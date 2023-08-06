# --------------------------------------------------------------------------- #
#   DisplayLang                                                               #
#                                                                             #
#   Copyright (c) 2020-2023 DisplayLang Contributors                          #
#                                                                             #
#   Licensed under the Apache License, Version 2.0 (the "License");           #
#   you may not use this file except in compliance with the License.          #
#   You may obtain a copy of the License at                                   #
#                                                                             #
#       http://www.apache.org/licenses/LICENSE-2.0                            #
#                                                                             #
#   Unless required by applicable law or agreed to in writing, software       #
#   distributed under the License is distributed on an "AS IS" BASIS,         #
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  #
#   See the License for the specific language governing permissions and       #
#   limitations under the License.                                            #
# --------------------------------------------------------------------------- #


"""Controlled evaluation of Python ASTs. """

import ast
import logging
import types

from .exceptions import ControlledEvaluationException, DisallowedCallable
from .visit import visitor_recurse


def is_builtin_method(m):
    """
    Try to identify built-in methods.

    Observe:

    >>> type(str.join)
    method_descriptor
    >>> type('foo'.join)
    builtin_function_or_method

    >>> repr(str.join)
    "<method 'join' of 'str' objects>"
    >>> repr('foo'.join)
    '<built-in method join of str object at 0x10ba8c8f0>'

    In the technical jargon of Python, a generic method like `str.join` of
    a built-in type is a "method descriptor," while the particular method like
    `'foo'.join` belonging to an instance of a built-in type is a "built-in
    method."

    Given any object, how do you determine if it's a built-in method?

    This is a good start:

    >>> import types
    >>> type('foo'.join) == types.BuiltinMethodType
    True

    but unfortunately it does not distinguish a built-in method from a built-in
    function:

    >>> type(len) == types.BuiltinMethodType
    True

    Nor does this:

    >>> type(len) == types.BuiltinFunctionType
    True
    >>> type('foo'.join) == types.BuiltinFunctionType
    True

    However, we can consider the qualname:

    >>> 'foo'.join.__qualname__
    'str.join'
    >>> len.__qualname__
    'len'

    which should have two segments for built-in methods, but just one segment
    for built-in functions.

    We can also consult the ``__self__`` attribute, which is equal to the
    builins module for built-in functions:

    >>> s = 'foo'
    >>> s.join.__self__ is s
    True
    >>> len.__self__
    <module 'builtins' (built-in)>

    This is an important test, because when we use this function to identify
    a built-in method, we are going to be passing that method's ``__self__``
    attribute as the first argument, and it sounds risky to go passing the
    builtins module as any argument to any function (even if it would be
    blocked by argument type checking).
    """
    q = getattr(m, '__qualname__', '')
    s = getattr(m, '__self__', None)
    return (
        type(m) == types.BuiltinMethodType and
        type(s) != types.ModuleType and
        len(q.split('.')) == 2
    )


def make_key_for_callable(callable):
    """
    One of our basic safety mechanisms is that we do not call any object
    that we are handed. Instead, we use the object we are handed to look up an
    ``AllowedCallable`` instance, and then we call that. Thus, we only ever
    call things that we constructed and approved in advance, not things users
    constructed.

    (Note: By using the `abstract_function_classes` and/or `allow_local_var_calls`
    kwargs of the `ControlledEvaluator` class, it is possible to make exceptions
    to this rule.)

    For this to work, we need a way to translate any given callable into a key,
    with which we can look up the corresponding ``AllowedCallable``. For most
    types of callables, this is easy: for built-in functions, user-defined
    functions, and user-defined classes, the callable itself can be used as
    the key. For bound methods of user-defined classes, we can use the
    ``__func__`` attribute, which points to the unbound function.

    For built-in methods, however, there is no ``__func__`` attribute, and we
    instead use their ``__qualname__`` attribute (which is a string).

    In order to understand the problem, we need to contrast built-in methods
    with the methods of user-defined classes. The great thing about the latter
    is that bound methods of user-defined classes have a ``__func__`` attribute,
    which is equal to the underlying method:

    >>> class Foo:
    >>>     def bar(self):
    >>>         return 42
    >>> f = Foo()
    >>> f.bar.__func__ == Foo.bar
    True

    This means that when we're defining an ``AllowedCallable`` for ``Foo.bar``,
    we can pass ``Foo.bar`` as the callable, and later, when a user tries to
    invoke `f.bar()`, we can use `f.bar.__func__` as the key.

    This does not work with built-in methods. The analogy is that ``f.bar`` is
    to ``Foo.bar`` as ``'foo'.join`` is to ``str.join``. The latter is called
    a "method descriptor." We would like ``'foo'.join`` to have a ``__func__``
    attribute, and we would like it to be equal to ``str.join``, but this is
    not the case:

    >>> hasattr('foo'.join, '__func__')
    False

    We cannot compare to the method desriptor directly either:

    >>> 'foo'.join == str.join
    False

    But the built-in method and its corresponding method descriptor do have the
    same qualname:

    >>> 'foo'.join.__qualname__
    'str.join'
    >>> str.join.__qualname__
    'str.join'

    Since for everything *except* built-in methods, the key is a callable (not
    a string), we can use the ``__qualname__`` of a built-in method as its key,
    without fear of this string colliding with any other key.

    Note that we must support both built-in methods and method descriptors
    here. We will encounter built-in methods while evaluating user code; we
    will encounter method descriptors while adding ``AllowedCallable``s to a
    ``ControlledEvaluator``. In both cases, we need to generate the same key.
    """
    if is_builtin_method(callable) or type(callable) == types.MethodDescriptorType:
        return callable.__qualname__
    elif type(callable) == types.MethodType:
        return callable.__func__
    return callable


def reject(msg='error', node=None, excep_class=ControlledEvaluationException):
    """Convenience method for raising exceptions (while parsing). """
    if node is not None:
        msg += f'\nAt line {node.lineno}, column {node.col_offset}.'
    raise excep_class(msg)


def safe_key_test(k, d):
    """
    Check whether a given object is a key in a given dictionary, returning
    False if the object is not hashable.

    :param k: the object that is the potential key
    :param d: the dictionary
    :return: boolean
    """
    try:
        return k in d
    except TypeError:
        return False


class ControlledEvaluator(ast.NodeTransformer):
    """
    Supports a subset of the Python language, and...

    * Only allows callables meeting one of the following conditions:
        (1) named under `abstract_function_classes` (if any)
        (2) belonging to local_vars, *if* this is enabled
        (3) on an explicit list of `AllowedCallable` instances, defined
            via the `add_allowed_callables()` method.

    * Supports limiting the size of operands to mult and pow (subclasses
      must override to implement this).
    """

    translate = {}
    pass_through = [
        'Load',
    ]
    banned_attributes = [
        '__globals__',
    ]
    # It is useful to note deliberately banned callables, for two reasons: (1) this
    # makes it clear that we haven't simply forgotten about these functions; we have
    # thought about them and decided not to allow them. (2) this gives us a chance to
    # record a helpful error message (if called for).
    banned_builtin_callables = {
        exec: None,
        eval: None,
        # The problem with `map` is that it carries out a function call which we do
        # not get to visit, meaning it gets around the safety provided by our
        # `visit_Call()` method. Display authors should use comprehensions instead.
        map: "`map` is not supported. Use a list comprehension instead.",
    }

    def __init__(self, basic_vars=None, local_vars=None,
                 allow_local_var_calls=False,
                 abstract_function_classes=None,
                 abstract_relation_classes=None):
        """

        :param basic_vars: dict mapping names to objects, defining variables
            that should be available during evaluation. As the name suggests,
            this is a place to define a "basis" for the namespace, i.e. a set
            of constants, functions, etc. which users should generally expect
            to be available. This is likely to be the same set, every time you
            evaluate user code.

        :param local_vars: dict mapping names to objects, defining variables
            that should be available during evaluation. This is a place to
            define variables that are special, for a particular evaluation.
            This is likely to be different each time you evaluate user code.

            This set is consulted first. Only if a name is missing here, will
            `basic_vars` be consulted.

        :param allow_local_var_calls: boolean, default False. If True, then
            if and when user code attempts to call any callable which is a value
            in `local_vars`, WE WILL CARRY OUT THE CALL WITHOUT FURTHER CHECKS.

            WARNING: If you enable this feature, you must be very careful about
            what can be in `local_vars`.

        :param abstract_function_classes: optional list of classes like
            SymPy's `UndefinedFunction` class, which are meant to be callable
            in an inert way, i.e. calling them doesn't do anything except
            produce a new symbolic object.

            WARNING: If user code contains an attempt to call any instance of
            any of these classes, WE WILL CARRY OUT THE CALL WITHOUT FURTHER
            CHECKS. Be SURE that classes you name here -- AND ANY AVAILABLE
            SUBCLASSES THEREOF -- truly are inert, i.e. don't actually do
            anything when you call them. ("Available" means: possible for
            user code to construct or otherwise obtain an instance of.)

        :param abstract_relation_classes: optional list of classes like
            SymPy's `Relational` class, which are possible return values of any
            of the comparison operators (`<`, `<=`, etc.), and which are meant
            to represent an abstract relation, in which the truth value is not
            known, or cannot be evaluated.

            The purpose of listing classes here is to short-circuit the behavior
            of the `visit_Compare()` method, and simply return the abstract
            relation class itself, instead of trying to return a boolean.
        """
        self.allowed_callables = {}
        self.dunder_callables = {}

        self.basic_vars = basic_vars or {}

        # Note: can't use `local_vars or {}` here, since that would make it
        # impossible for you to pass an empty dictionary in which to receive
        # vars defined in the process of evaluation (in subclasses that support
        # this).
        self.local_vars = {} if local_vars is None else local_vars

        # Subclasses may wish to provide support for language constructs that
        # involve the use of bound variables (such as list comprehensions).
        self.bound_vars = {}

        self.allow_local_var_calls = allow_local_var_calls
        self.abstract_function_classes = tuple(abstract_function_classes or [])
        self.abstract_relation_classes = tuple(abstract_relation_classes or [])

    def add_allowed_callables(self, acs):
        """
        Add a list (or other iterable) of ``AllowedCallable``s.

        Anything you add here can be invoked via user code, as long as the
        user-given arguments satisfy the requirements of the ``AllowedCallable``.
        """
        for ac in acs:
            if ac.is_dunder_call:
                self.dunder_callables[ac.method_of] = ac
            else:
                k = make_key_for_callable(ac.callable)
                self.allowed_callables[k] = ac

    def set_local_vars(self, local_vars):
        """
        Reset the ``local_vars`` dict.
        This is useful if you want to re-use a single instance of this class
        to peform multiple evaluations.
        """
        self.local_vars = local_vars

    def generic_visit(self, node):
        """
        AST node types for which we have not written special visitor methods
        are handled here. They have three possible fates:
        (1) If they are listed under "pass_through" then they are returned
            unaltered;
        (2) If they are a key in the "translate" lookup then they are replaced
            by their lookup value;
        (3) Otherwise they are considered unsupported node types, and we raise
            an exception.
        """
        classname = node.__class__.__name__
        if classname in self.pass_through:
            return node
        elif classname in self.translate:
            return self.translate[classname]
        msg = f'Unsupported node type, `{classname}`.'
        msg += ' This means you are trying to use a feature of the Python'
        msg += ' language that is not supported in this restricted sublanguage.'
        reject(msg, node)

    def recurse(self, node, fields=None):
        """
        Visitor methods may start with a call to this method, in order
        to achieve a bottom-up traversal of the tree.

        @param node: the ast node on which to recurse
        @param fields: pass a set or list of field names to limit processing
            to these fields only.

        Compare `ast.NodeTransformer.generic_visit`.
        """
        visitor_recurse(self, node, fields=fields)

    def visit_keyword(self, node):
        """This node type is involved in parsing kwargs in function calls."""
        self.recurse(node)
        return node.arg, node.value

    def visit_Call(self, node):
        self.recurse(node)
        F = node.func
        A = node.args or []
        K = {k: v for k, v in node.keywords}

        self.log_call_attempt(F, A, K)

        # Note: we make use of `safe_key_test()` twice below, because `F` could
        # be an instance of an unhashable class, and we are trying to call its
        # `__call__()` method.

        if safe_key_test(F, self.banned_builtin_callables):
            logging.info('<banned builtin>')
            help = self.banned_builtin_callables.get(F)
            msg = help or f'Disallowed callable "{F.__name__}".'
            reject(msg, node, excep_class=DisallowedCallable)

        if isinstance(F, self.abstract_function_classes):
            logging.info('<called as abstract function>')
            return F(*A, **K)

        if self.allow_local_var_calls and F in self.local_vars.values():
            logging.info('<called as local var>')
            return F(*A, **K)

        if type(F) in self.dunder_callables:
            logging.info('<called as dunder callable>')
            A = [F] + A
            dc = self.dunder_callables[type(F)]
            return dc(*A, **K)

        if is_builtin_method(F) or type(F) == types.MethodType:
            # When `F` is a bound method, the callable we end up calling is
            # always the unbound version. So must prepend the `self` arg.
            A = [F.__self__] + A

        key = make_key_for_callable(F)
        if safe_key_test(key, self.allowed_callables):
            logging.info('<called as AllowedCallable>')
            ac = self.allowed_callables[key]
            return ac(*A, **K)

        logging.info('<disallowed>')
        msg = f'Disallowed callable: {getattr(F, "__module__", "<nomod>")}.{getattr(F, "__qualname__", "<noname>")}'
        reject(msg, node=node, excep_class=DisallowedCallable)

    def log_call_attempt(self, F, A, K):
        mod = getattr(F, "__module__", "<nomod>")
        name = getattr(F, "__qualname__", "<noname>")
        class_ = str(getattr(F, "__class__", "<noclass>"))
        arg_types = [str(type(a)) for a in A]
        kwarg_types = {k: str(type(v)) for k, v in K.items()}
        logging.info('mod=%s;name=%s;class=%s;args=%s;kwargs=%s',
                     mod, name, class_, arg_types, kwarg_types)
        logging.debug('mod=%s;name=%s', mod, name, stack_info=True)

    def visit_Name(self, node):
        name = node.id
        if name in self.bound_vars:
            return self.bound_vars[name]
        if name in self.local_vars:
            return self.local_vars[name]
        if name in self.basic_vars:
            return self.basic_vars[name]
        msg = f'Unknown name: {name}'
        reject(msg, node)

    def visit_Attribute(self, node):
        self.recurse(node)
        A = node.attr
        # Here we have an extra precaution against things like
        #   `func.__globals__["__builtins__"]["exec"]`
        # To be clear, the `visit_Call` method should prevent trouble even if
        # `exec` could be accessed, but we believe in redundancy.
        if A in self.banned_attributes:
            reject(f'Attribute "{A}" not allowed.', node)
        else:
            # Note: We deliberately do not use `hasattr`, or provide a third
            # (default) arg. If the user has made a mistake, we want them to
            # see the corresponding error message.
            return getattr(node.value, A)

    def visit_BinOp(self, node):
        # First note whether it's Pow or Mult.
        is_pow = isinstance(node.op, ast.Pow)
        is_mult = isinstance(node.op, ast.Mult)
        self.recurse(node)
        L, R = node.left, node.right
        if is_pow:
            self.pow_check(L, R)
        if is_mult:
            self.mult_check(L, R)
        return node.op(L, R)

    def pow_check(self, b, e):
        """
        Subclasses may wish to override.
        This is a chance to raise an exception and prevent an operation on
        arguments that are too large.
        """
        pass

    def mult_check(self, a, b):
        """
        Subclasses may wish to override.
        This is a chance to raise an exception and prevent an operation on
        arguments that are too large.
        """
        pass

    def visit_Compare(self, node):
        """
        Normally, evaluates a chain of comparisons and returns a boolean.
        If abstract relation classes were named, and if a comparison in user
        code results in construction of an instance of one of these classes,
        then the instance is returned.
        """
        self.recurse(node)
        L = node.left
        for test, R in zip(node.ops, node.comparators):
            cmp = test(L, R)
            if isinstance(cmp, self.abstract_relation_classes):
                return cmp
            if not cmp:
                return False
            L = R
        return True


class ExpressionEvaluator(ControlledEvaluator):

    translate = {
        # Binary operators
        'Add': lambda a, b: a + b,
        'Sub': lambda a, b: a - b,
        'Mult': lambda a, b: a * b,
        'Div': lambda a, b: a / b,
        'FloorDiv': lambda a, b: a // b,
        'Mod': lambda a, b: a % b,
        'Pow': lambda a, b: a ** b,
        'LShift': lambda a, b: a << b,
        'RShift': lambda a, b: a >> b,
        'BitOr': lambda a, b: a | b,
        'BitXor': lambda a, b: a ^ b,
        'BitAnd': lambda a, b: a & b,
        'MatMult': lambda a, b: a @ b,
        # Unary operators
        'UAdd': lambda a: +a,
        'USub': lambda a: -a,
        'Not': lambda a: not a,
        'Invert': lambda a: ~a,
        # Boolean operators
        'And': lambda cs: all(cs),
        'Or': lambda ds: any(ds),
        # Comparisons
        'Eq': lambda a, b: a == b,
        'NotEq': lambda a, b: a != b,
        'Lt': lambda a, b: a < b,
        'LtE': lambda a, b: a <= b,
        'Gt': lambda a, b: a > b,
        'GtE': lambda a, b: a >= b,
        'Is': lambda a, b: a is b,
        'IsNot': lambda a, b: a is not b,
        'In': lambda a, b: a in b,
        'NotIn': lambda a, b: a not in b,
    }

    def visit_Expr(self, node):
        self.recurse(node)
        return node.value

    def visit_Constant(self, node):
        return node.value

    def visit_BoolOp(self, node):
        self.recurse(node)
        return node.op(node.values)

    def visit_UnaryOp(self, node):
        self.recurse(node)
        return node.op(node.operand)

    def visit_Dict(self, node):
        self.recurse(node)
        return {k:v for k, v in zip(node.keys, node.values)}

    def visit_List(self, node):
        self.recurse(node)
        return node.elts

    def visit_Tuple(self, node):
        self.recurse(node)
        return tuple(node.elts)

    def visit_Set(self, node):
        self.recurse(node)
        return set(node.elts)

    def visit_Subscript(self, node):
        self.recurse(node)
        v, s = node.value, node.slice
        return v[s]

    def visit_Index(self, node):
        self.recurse(node)
        return node.value

    def visit_Slice(self, node):
        self.recurse(node)
        return slice(node.lower, node.upper, node.step)


def evaluate_expression(expression_evaluator, s):
    """
    Parse a string and apply an ExpressionEvaluator to it.

    :param expression_evaluator: ExpressionEvaluator that should
        visit the AST.
    :param s: the string to be parsed into an AST, then visited.
    :return: the return value of `expression_evaluator.visit()`.
    """
    node = ast.parse(s)
    node = ast.Expr(node.body[0].value)
    return expression_evaluator.visit(node)
