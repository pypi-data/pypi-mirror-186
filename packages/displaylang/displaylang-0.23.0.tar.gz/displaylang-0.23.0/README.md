# DisplayLang

The problem: Support a limited subset of the Python language, powerful enough
to allow authors to conveniently build HTML displays based on SymPy classes,
but limited enough to offer a reasonable expectation of safe evaluation.

We call the language "DisplayLang". It was originally designed for authoring
example explorers in Proofscape, but it attempts to solve a fairly general
problem, so should be more broadly useful.

In fact the set of `AllowedCallable`s for SymPy functions and classes which
can be used in Proofscape is defined in the
[pfsc-examp](https://github.com/proofscape/pfsc-examp) project, not here.
This project is more foundational, defining AST node traversers, providing
the basic framework for defining `AllowedCallable`s, and defining these for
built-in Python functions and methods.

## The language

The syntax is defined by three things:

* Which statement and expression types in the Python language we support.
* Which callables we allow to be called.
* For the allowed callables, what types the arguments are allowed to be, and,
  when they are strings, what regexes the strings must match.

The reason for paying special attention to string arguments is that there are
functions that are definitely unsafe if they can be passed arbitrary
strings, but are probably safe as long as either we don't allow strings to be
passed at all, or we allow only strings of certain restricted forms.

Of course we need to be careful about built-in Python callables, such
as `exec` and `eval`, not to mention things like `os.system`. So our overall
solution is to ban all function calls outside a finite, curated, set of
approved calls. The set is expected to grow over time, in response to user
demand.

Among banned statement types are `import` statements, which supports the
providing of only a finite, curated set of available _names_.

## Getting started

Better docs are on the way, but for now we offer the following hints for
getting started:

* See the `displaylang.build.DisplayLangProcessor.process()` method, for the
  core code that processes a string of DisplayLang.
  - See also the `displaylang.build.make_displaylang_processor()` convenience
    function for building a `DisplayLangProcessor` instance.

* Check out the `displaylang.allow.AllowedCallable.__init__()` method to see
  how an `AllowedCallable` is defined.
