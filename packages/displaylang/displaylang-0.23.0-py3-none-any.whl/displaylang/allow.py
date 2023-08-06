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


"""Allowed callables, for safer parsing. """

from enum import Enum
import re
import types

from typeguard import check_type

from .exceptions import BadArgs, CannotCall


CNAME_PATTERN = re.compile(r'[_a-zA-Z]\w*$', re.ASCII)
UNICODE_WORD = re.compile(r'\w+$')
# Note: for StrPermType.NUMBER, we enforce non-emptiness not in the regex,
# but in the `string_is_permitted()` function. See below.
# Also note that these regexes are not meant to exclude all but syntactically
# valid Python. We are happy to allow the Python ast parser to weed out invalid
# forms. These regexes are only meant to limit strings to "safe" forms.
NUMBER_PATTERN = re.compile(r'\d*(\.\d*)?([eE][-+]?\d+)?$')


class StrPermType(Enum):
    # Reject all strings:
    NONE = "NONE"
    # Any string is accepted:
    ANY = "ANY"
    # Accept only CNAMEs, i.e. `[_a-zA-Z]\w*` with `re.ASCII` flag:
    CNAME = "CNAME"
    # Accept a comma-delimited list (ignoring whitespace) of CNAMEs:
    CNAME_CDL = "CNAME_CDL"
    # Accept any nonempty Unicode word:
    UWORD = "UWORD"
    # Accept a comma-delimited list (ignoring whitespace) of UWORDs:
    UWORD_CDL = "UWORD_CDL"
    # Any numeric literal (int or float)
    NUMBER = "NUMBER"
    # + or -
    SIGN = "SIGN"


def string_is_permitted(s, perm_type):
    """
    Check whether a string is acceptable under a given string permission type.

    @param s: str
        The string to be checked.
    @param perm_type:  StrPermType
        The permission type that the string is expected to satisfy.
    @return: boolean, True iff the string is acceptable.
    """
    if perm_type == StrPermType.NONE:
        return False
    if perm_type == StrPermType.ANY:
        return True
    if perm_type == StrPermType.CNAME:
        return CNAME_PATTERN.match(s)
    if perm_type == StrPermType.CNAME_CDL:
        parts = [p.strip() for p in s.split(',')]
        return all(CNAME_PATTERN.match(p) for p in parts)
    if perm_type == StrPermType.UWORD:
        return UNICODE_WORD.match(s)
    if perm_type == StrPermType.UWORD_CDL:
        parts = [p.strip() for p in s.split(',')]
        return all(UNICODE_WORD.match(p) for p in parts)
    if perm_type == StrPermType.NUMBER:
        return s and NUMBER_PATTERN.match(s)
    if perm_type == StrPermType.SIGN:
        return s in ["+", "-"]
    return False


class ArgSpec:
    """
    Define the allowed values for a single argument.
    """

    def __init__(self, t=None, s=None, f=None):
        """
        @param t: a type that the argument is allowed to be.

            A type can be any built-in type (except `str`, see below),
            or any user-defined class,
            or any of the type hint constructions listed
            [here](https://typeguard.readthedocs.io/en/latest/userguide.html#supported-typing-types)
            from the `typing` module.

            You cannot allow strings by listing `str` here. If you want to
            allow strings you must use the `s` kwarg.

        @param s: StrPermType or None. If a StrPermType, then the
            argument is allowed to be a string iff it matches this
            type.

        @param f: a fixed set of alternative values that the argument must
            equal. Pass any iterable. Overrules s and t completely.

        Note: If f is not given, then t and s are disjunctive, i.e. an argument
        is accepted if it passes _either_ of their tests. If f is given, both
        t and s are ignored.
        """
        self.typehint = t
        self.strings = s
        self.fixed = f

    def __str__(self):
        p = []
        if self.fixed is not None:
            p.append(f'in: {self.fixed}')
        else:
            if self.typehint is not None:
                p.append(str(self.typehint))
            if self.strings is not None:
                p.append(f'str: {self.strings}')
        return ' or '.join(p)

    @classmethod
    def convert(cls, other):
        """
        Convert something other than an `ArgSpec` into an `ArgSpec`.

        An `ArgSpec` or a `Tail` is left unchanged.
        A `StrPermType` `s` is converted into an `ArgSpec` with `s=s`.
        Anything else is assumed to be a value for the `t` kwarg.

        Note: You cannot use this method to construct an `ArgSpec` with
        the "fixed" (`f`) kwarg.
        """
        if isinstance(other, (ArgSpec, Tail)):
            return other
        elif isinstance(other, StrPermType):
            return cls(s=other)
        else:
            return cls(other)

    def ok(self, arg):
        """
        Test whether a given arg matches the spec.
        """
        if self.fixed is not None:
            return arg in self.fixed
        elif isinstance(arg, str):
            if isinstance(self.strings, StrPermType):
                return string_is_permitted(arg, self.strings)
            return False
        else:
            try:
                check_type('arg', arg, self.typehint)
            except TypeError:
                return False
            else:
                return True


class Tail:
    """
    Provide an arg spec for the tail end of a free list `*args` of positional args.
    """

    def __init__(self, spec):
        """
        :param spec: an `ArgSpec` or anything convertible thereto via
            `ArgSpec.convert()`.
        """
        self.spec = ArgSpec.convert(spec)

    def ok(self, args):
        """Check whether an iterable of arguments passes the spec."""
        return all(self.spec.ok(a) for a in args)

    def first_failing_index(self, args):
        """
        Check an iterable of arguments and either return the index of the
        first argument that failed the spec, or -1 if they all passed.
        """
        for i, a in enumerate(args):
            if not self.spec.ok(a):
                return i
        return -1


class CheckedArgs:
    """
    Represents the result of checking a given pair (A0, K0) of positional and
    keyword args against a Signature.

    An instance of this class will contain a pair (self.A, self.K)
    of args that are okay to be passed on to the callable in question. Only
    these args, not the given ones, must be passed onward. This is because
    the given (A0, K0) may contain keyword args passed positionally, and we
    must be sure that these go to the right arg. There could be a difference
    because `AllowedCallable`s are sometimes a work-in-progress, in which not
    every keyword arg yet has a typedef. In (self.A, self.K), keyword args are
    never passed positionally; they are always moved into self.K.

    Example:

    Consider a function,

        def foo(bar, spam=None, baz=None):
            ...

    and suppose the AllowedCallable that has been defined is a work in progress,

        ac = AllowedCallable(foo, [int], {baz=StrPermType.ANY})

    in which the developer has not yet made the arg spec for the `spam` kwarg.
    Note: In such a case, the developer _should_ have set `incomplete=True`
    (see `AllowedCallable.__init__()`), to disallow positionally passed kwargs.

    When we then check the function call

        foo(1, 'lorem.ipsum[0]')

    against `ac`, we will approve the string 'lorem.ipsum[0]' for use with
    kwarg `baz`. However, if we just forwarded the args to `foo` as they are,
    then kwarg `spam` would receive this string. This could be a security
    vulnerability.
    """

    def __init__(self, signature, checked_pos_args, checked_kwargs):
        self.signature = signature
        self.A = checked_pos_args
        self.K = checked_kwargs


class Signature:
    """
    Represents a single acceptable function signature, including arg specs for
    both positional and keyword arguments.
    """

    def __init__(self, allowed_callable, pos_arg_specs, kwarg_specs, incomplete):
        """
        :param allowed_callable: the AllowedCallable this Signature is for.
        :param pos_arg_specs: list of ArgSpecs or anything convertible thereto.
        :param kwarg_specs: dict of ArgSpecs or anything convertible thereto.
        :param incomplete: boolean saying whether `kwarg_specs` is complete
            or omits definitions for some kwargs of the intended callable.
        """
        self.ac = allowed_callable
        self.incomplete = incomplete

        pos_arg_specs = [ArgSpec.convert(s) for s in pos_arg_specs]
        self.req_arg_specs = []
        self.tail = None
        if pos_arg_specs:
            if isinstance(pos_arg_specs[-1], Tail):
                self.req_arg_specs = pos_arg_specs[:-1]
                self.tail = pos_arg_specs[-1]
            else:
                self.req_arg_specs = pos_arg_specs
        self.num_req_args = len(self.req_arg_specs)

        self.kwarg_specs = {k: ArgSpec.convert(v) for k, v in kwarg_specs.items()}
        self.num_kwargs = len(self.kwarg_specs)

    def write_arg_err_msg(self, arg_spec, pos=None, kw=None):
        if pos is not None:
            msg = f'For positional arg {pos}'
        else:
            msg = f'For keyword arg "{kw}"'
        msg += f' of the `{self.ac.full_name}` function, arg spec is: {arg_spec}.'
        return msg

    def check_args(self, A, K):
        """
        Check the given arguments for any violation of the type permissions
        for this signature. If there is any violotion, a BadArgs is raised.

        @param A: list of positional args
        @param K: dict of keyword args
        @raises: BadArgs if any arguments violate type permissions
        @return: CheckedArgs instance, in which there are no ambiguities,
            namely, keyword args are passed only as such, never positionally.
        """
        N = len(A)
        n = self.num_req_args
        allow_positional_kwargs = not self.incomplete

        if N < n:
            raise BadArgs(f'Missing positional args to function `{self.ac.full_name}`.')

        A0, A_tail = A[:n], A[n:]

        for i, (a, spec) in enumerate(zip(A0, self.req_arg_specs)):
            if not spec.ok(a):
                raise BadArgs(self.write_arg_err_msg(spec, pos=i))

        A1, K1 = A, K

        if A_tail:
            if self.tail:
                i = self.tail.first_failing_index(A_tail)
                if i >= 0:
                    raise BadArgs(self.write_arg_err_msg(self.tail.spec, pos=i))
            elif allow_positional_kwargs:
                if len(A_tail) > self.num_kwargs:
                    raise BadArgs(f'Too many positional args to function `{self.ac.full_name}`.')
                A1 = A0
                K1 = {k: a for k, a in zip(self.kwarg_specs.keys(), A_tail)}
                for k, v in K.items():
                    if k in K1:
                        raise BadArgs(f'{self.ac.full_name} got multiple values for argument {k}')
                    else:
                        K1[k] = v
            else:
                raise BadArgs(f'Positional kwargs are not allowed for {self.ac.full_name}')

        for k, v in K1.items():
            spec = self.kwarg_specs.get(k)
            if spec is None:
                raise BadArgs(f'No arg spec for keyword arg `{k}` to function `{self.ac.full_name}`.')
            if not spec.ok(v):
                raise BadArgs(self.write_arg_err_msg(spec, kw=k))

        return CheckedArgs(self, A1, K1)


class AllowedCallable:

    def __init__(self, callable, pos_arg_specs, kwarg_specs=None,
                 name=None, method_of=None, classmethod_of=None,
                 incomplete=False):
        """
        @param callable: the callable itself, which we represent.
            NOTE: Among dunder methods (`Foo.__init__`, `Foo.__call__`,
            `Foo.__str__`, `Foo.__add__`, etc.), only `Foo.__call__` should ever
            be passed here, which is how you say that you want instances of class
            `Foo` to be callable. (In that case, must pass `method_of=Foo`.)

            When you want class `Foo` to be constructable, simply pass `Foo`
            here, not `Foo.__init__`.

            As for any other dunder methods like `Foo.__str__` or `Foo.__add__`,
            the decision for now is that these are ALWAYS ALLOWED, and WITH NO
            ARG TYPE CHECKING. In the future we may switch to a more stringent
            system where these methods too have to be individually approved,
            but for now this is how it works.

        @param pos_arg_specs: In the "basic" case, this is a list of arg specs,
            one for each positional arg the callable accepts. Each spec can be
            an actual `ArgSpec` instance, or anything convertible thereto (by
            the `ArgSpec.convert()` class method). The last spec can be a
            `Tail` instance.

            In the "advanced" case, this can be a list of such lists, as a way
            of specifying alternative function signatures. For example, maybe
            the function either accepts two ints, or one float.

        @param kwarg_specs: In the "basic" case, this is a dictionary of arg
            specs, one for each keyword arg the callable accepts. Omitting the
            spec for a keyword arg means we have not allowed anything to be
            passed for that arg. Each spec can be an actual `ArgSpec` instance,
            or anything convertible thereto. In the "advanced" case, this can
            be a list of such dictionaries.

            If `pos_arg_specs` is a list of lists, but `kwarg_specs` is a single
            dictionary, then these are the kwarg specs for every alternative
            list of positional arg specs. If `kwarg_specs` is also a list then
            dictionaries after the first inherit from the previous one and
            override only those entries they define. If the list of dicts is
            shorter than `pos_arg_specs`, empty dicts are inserted at the end
            to make it the same length.

        @param name: If `None`, the name of the callable will be automatically
            determined from its `__qualname__` attribute. If a string, this
            name will be used instead.

            Example: For the SymPy `Matrix` class,
            `Matrix.__qualname__` returns the name "MutableDenseMatrix", instead
            of the name "Matrix" that we probably want. For this case, "Matrix"
            could be passed as the value of the `name` parameter.

            If `callable.__qualname__` is undefined (example: the SymPy `S`
            object), then you must supply a name here.

            The intention is that this name be usable as the name of this callable
            when parsing Python code where this callable should be available.

        @param method_of: When the callable is an instance method, you must provide
            the arg spec for the first (i.e. `self`) argument here, and not in
            `pos_arg_specs`. May be an actual `ArgSpec` instance, or anything
            convertible thereto. May be a list of alternatives of equal length
            to `pos_arg_specs` when that is a list of lists.

        @param classmethod_of: When the callable is a @classmethod, you must
            provide the class for the first (i.e. `cls`) argument here, and not
            in `pos_arg_specs`. Should simply be the class itself (not an `ArgSpec`
            instance). May be a list of alternatives of equal length to
            `pos_arg_specs` when that is a list of lists.

        @param incomplete: If True, we will not allow kwargs to be passed
            positionally. This is meant to support gradual development, so that
            a developer can define an AllowedCallable in which some, but not yet
            all, of the kwargs have type definitions. If False (the default), then
            kwargs passed positionally will be mapped to kwargs in the order
            defined in `kwarg_specs`.

            Note: If the kwarg specs are incomplete, but the developer forgets
            to set `incomplete` to True, it will lead to unexpected
            behavior, but not dangerous behavior, thanks to the use of
            `CheckedArgs`. See docstring for that class for more.
        """
        # Replace bound methods with their underlying function.
        # This seems to happen when `callable` is a `@classmethod`, but not
        # when it's an ordinary instance method.
        if type(callable) == types.MethodType:
            callable = callable.__func__

        self.callable = callable
        self.method_of = method_of
        self.incomplete = incomplete

        qualname = getattr(callable, '__qualname__', None)
        mo_given = ((isinstance(method_of, list) and len(method_of) > 0) or method_of is not None)
        co_given = ((isinstance(classmethod_of, list) and len(classmethod_of) > 0) or classmethod_of is not None)
        lead_arg_given = mo_given or co_given

        if qualname is None:
            if not name:
                raise ValueError('Callable has no __qualname__. Must supply a name.')
        else:
            dotted = (qualname.find('.') >= 0)
            if dotted and not lead_arg_given:
                raise ValueError(
                    'Callable does not appear to be a top-level function or class.'
                    ' If an instance- or class-method, you must define a `method_of`'
                    ' or `classmethod_of`, respectively.'
                )
            if lead_arg_given and not dotted:
                raise ValueError(
                    'Callable appears to be a top-level function or class.'
                    ' You should not define a `method_of` or `classmethod_of`.'
                )

        self._name = name or qualname

        P, K = pos_arg_specs, (kwarg_specs or {})
        if not isinstance(P, list):
            raise ValueError('pos_arg_specs must be a list')
        if len(P) == 0 or not isinstance(P[0], list):
            P = [P]

        if lead_arg_given:
            if co_given:
                L = [classmethod_of] if not isinstance(classmethod_of, list) else classmethod_of
                L = [ArgSpec(f=[c]) for c in L]
            else:
                L = [method_of] if not isinstance(method_of, list) else method_of
            d = len(P) - len(L)
            while d > 0:
                L.append(L[-1])
                d -= 1
            P1 = []
            for a, p in zip(L, P):
                P1.append([a] + p)
            P = P1

        if isinstance(K, dict):
            K = [K]
        d = len(P) - len(K)
        while d > 0:
            K.append({})
            d -= 1

        self.alternatives = []
        prev_k = {}
        for p, k0 in zip(P, K):
            k1 = {**prev_k, **k0}
            self.alternatives.append(Signature(self, p, k1, incomplete))
            prev_k = k1

    @property
    def name(self):
        return self._name

    @property
    def full_name(self):
        module = getattr(self.callable, '__module__', '<no_module>')
        return f'{module}.{self.name}'

    @property
    def is_dunder_call(self):
        """
        Say whether this `AllowedCallable` represents the `.__call__()` method
        of some class.
        """
        return (
            type(self.method_of) is type and
            self.callable is getattr(self.method_of, '__call__', None)
        )

    def __call__(self, *args, **kwargs):
        """
        Call our callable and return the result, but only if the args and kwargs
        satisfied one of our allowed signatures. Raise `CannotCall` if no
        signature was satisfied.
        """
        result = self.check_args(args, kwargs)
        if isinstance(result, CheckedArgs):
            A1, K1 = result.A, result.K
            return self.callable(*A1, **K1)
        raise CannotCall(result)

    def check_args(self, A, K):
        """
        Check the given arguments to see if they satisfy any of the alternative
        signautres allowed for this callable.

        @param A: list of positional args
        @param K: dict of keyword args
        @return: the CheckedArgs for the first Signature that was satisfied, or
            else a list of the BadArgs exceptions raised by each of the Signatures.
        """
        badArgExceps = []
        for sig in self.alternatives:
            try:
                checked_args = sig.check_args(A, K)
            except BadArgs as ba:
                badArgExceps.append(ba)
            else:
                return checked_args
        return badArgExceps
