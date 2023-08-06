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

import pytest

from displaylang.allow import AllowedCallable
from displaylang.evaluate import (
    DisallowedCallable, ExpressionEvaluator, evaluate_expression,
)


class AbstractFunction:

    def __call__(self, *args, **kwargs):
        return 42


class InstancesCanBeCalled:

    def __call__(self, a, b, c):
        return a + b + c


class DoNotCall:

    def __call__(self, *args, **kwargs):
        assert False


def a_local_function(a):
    return 2*a


basic_vars = {
    "exec": exec,
    "eval": eval,
    "map": map,
    "AbstractFunction": AbstractFunction,
    "InstancesCanBeCalled": InstancesCanBeCalled,
    "DoNotCall": DoNotCall,
}

local_vars = {
    "a_local_function": a_local_function,
}

"""
We want to test the various types of callables that may or may not be allowed
by `ControlledEvaluator.visit_Call()`, depending on how the evaluator is
constructed.

For our tests, we form two evaluators, which we call "basic" and "advanced".

In both, we make available all function and class _names_ on which we want
our tests to be based. This is so that no rejection is ever caused by a name
simply being absent. We want the callables to be obtained, and then rejected.

Also in both evaluators, we allow the class constructors for our three classes,
`AbstractFunction`, `InstancesCanBeCalled`, and `DoNotCall`, as callables.
Again, we don't want rejections to be based on attempts to _construct_ instances
of these classes; instead, we are interested in seeing what happens when you
attempt to _call_ an _instance_.

In the "basic" evaluator, we do not add any special features:
    * We do not allow local var calls.
    * We do not name any abstract function classes.
    * We do not add any dunder callables.

In the "advanced" evaluator, we do use all the special features:
    * We do allow local var calls.
    * We name `AbstractFunction` as an abstract function class.
    * We set `InstancesCanBeCalled` as a dunder callable.

The unit tests then check that we get the expected rejections and allowed calls.
"""

class_constructors = [
    AllowedCallable(AbstractFunction, []),
    AllowedCallable(InstancesCanBeCalled, []),
    AllowedCallable(DoNotCall, []),
]

basic_evaluator = ExpressionEvaluator(basic_vars, local_vars)
basic_evaluator.add_allowed_callables(class_constructors)

advanced_evaluator = ExpressionEvaluator(
    basic_vars, local_vars,
    allow_local_var_calls=True,
    abstract_function_classes=[AbstractFunction]
)
advanced_evaluator.add_allowed_callables(class_constructors)
advanced_evaluator.add_allowed_callables([
    AllowedCallable(InstancesCanBeCalled.__call__, [int, int, int],
                    method_of=InstancesCanBeCalled),
])


@pytest.mark.parametrize('s', [
    'exec("foo")',
    'eval("foo")',
    'map(eval, ["foo", "bar"])',
    'DoNotCall()("foo")',
    'AbstractFunction()("foo")',
    'InstancesCanBeCalled()(1, 2, 3)',
    'a_local_function(5)',
])
def test_basic_evaluator_reject(s):
    with pytest.raises(DisallowedCallable):
        evaluate_expression(basic_evaluator, s)


@pytest.mark.parametrize('s', [
    'exec("foo")',
    'eval("foo")',
    'map(eval, ["foo", "bar"])',
    'DoNotCall()("foo")',
])
def test_advanced_evaluator_reject(s):
    with pytest.raises(DisallowedCallable):
        evaluate_expression(advanced_evaluator, s)


@pytest.mark.parametrize('s, r', [
    ['AbstractFunction()("foo")', 42],
    ['InstancesCanBeCalled()(1, 2, 3)', 6],
    ['a_local_function(5)', 10],
])
def test_advanced_evaluator_allow(s, r):
    assert evaluate_expression(advanced_evaluator, s) == r
