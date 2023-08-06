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

from displaylang.allow import AllowedCallable, Tail
from displaylang.exceptions import BadArgs, CannotCall


def foo(a, b, c=3, d=4):
    return sum([a, 2*b, 3*c, 4*d])


def bar(a, b, *c, d=4):
    return sum([a, 2*b, 3*sum(c), 4*d])


def test_check_args():
    # kwargs complete:
    ac_foo_1 = AllowedCallable(foo, [int, int], {'c': int, 'd': int})
    # kwargs incomplete, and marked as such:
    ac_foo_2 = AllowedCallable(foo, [int, int], {'d': int}, incomplete=True)
    # kwargs incomplete, forgot to mark as such:
    ac_foo_3 = AllowedCallable(foo, [int, int], {'d': int})
    # accepts a tail, kwargs complete:
    ac_bar = AllowedCallable(bar, [int, int, Tail(int)], {'d': int})

    # Not enough positional args
    with pytest.raises(CannotCall):
        ac_foo_1(1)
    # Malformed positional arg
    with pytest.raises(CannotCall):
        ac_foo_1(1, 'bar')

    # Kwargs can be omitted
    assert ac_foo_1(1, 1) == 28
    # Kwargs can be given
    assert ac_foo_1(1, 1, c=1) == 22
    # Extra positional args go to kwargs, in order
    assert ac_foo_1(1, 1, 1, 2) == 14
    # Cannot absorb more extra pos args than there are kwargs
    with pytest.raises(CannotCall):
        ac_foo_1(1, 2, 3, 4, 5)
    # Do not accept multiple values for a single kwarg
    with pytest.raises(CannotCall):
        ac_foo_1(1, 2, 3, 4, d=4)

    # Extra positional args not allowed, when kwargs marked as incomplete
    with pytest.raises(CannotCall):
        ac_foo_2(1, 1, 1)

    # Extra positional args converted to kwargs, when allowed
    signature = ac_foo_1.alternatives[0]
    checked_args = signature.check_args([1, 1, 1, 2], {})
    assert checked_args.A == [1, 1]
    assert checked_args.K == {'c': 1, 'd': 2}

    # If kwargs incomplete, and marked as such, Signature raises BadArgs on
    # extra pos arg.
    signature = ac_foo_2.alternatives[0]
    with pytest.raises(BadArgs):
        signature.check_args([1, 1, 2], {})

    # If kwargs incomplete, but dev forgot to mark it as such, still convert
    # extra positional arg to the kwarg against which it was checked.
    signature = ac_foo_3.alternatives[0]
    checked_args = signature.check_args([1, 1, 2], {})
    assert checked_args.A == [1, 1]
    assert checked_args.K == {'d': 2}

    # Tail args accepted
    assert ac_bar(1, 1, 2, 2, 2, d=5) == 41
    # Empty tail okay
    assert ac_bar(1, 1, d=5) == 23
    # Malformed tail arg
    with pytest.raises(CannotCall):
        ac_bar(1, 1, 2, 2, '2', d=5)
    # Malformed kwarg
    with pytest.raises(CannotCall):
        ac_bar(1, 1, d='5')
    # Unknown kwarg
    with pytest.raises(CannotCall):
        ac_bar(1, 1, e=5)
