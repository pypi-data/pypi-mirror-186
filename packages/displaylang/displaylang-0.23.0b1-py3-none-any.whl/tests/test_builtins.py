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

from displaylang.exceptions import CannotCall
from displaylang.build import basic_displaylang_processor


@pytest.mark.parametrize('code', [
    'len([1, 2, 3])',
    'len("foo")',
    'range(3)',
    'range(1, 4)',
    'range(1, 5, 2)',
    'str(3)',
    'str([1, 2, 3])',
    'sum([1, 2, 3])',
    'sum([1, 2, 3], 4)',
    'zip([1, 2, 3], [4, 5, 6])',
    '[1, 2, 3].append(True)',
    '[1, 2, 3].extend([True, False])',
    '",".join(["foo", "bar"])',
    '"FOO".lower()',
    '"foo".replace("o", "u")',
    '"foo bar".split()',
    '"foo bar".split("o b")',
    '"foo".upper()',
])
def test_allow_call(code):
    """
    Test that calls go through without raising any exception.
    """
    code += '\nreturn "foo"'
    basic_displaylang_processor.process(code, {})


@pytest.mark.parametrize('code', [
    'len(True)',
    'range("3")',
    'str(1, 2)',
    'sum(1, 2, 3)',
    'zip([1, 2, 3], True)',
    '[1, 2, 3].append(True, False)',
    '[1, 2, 3].extend(True)',
    '",".join([1, 2, 3])',
    '"FOO".lower(True)',
    '"foo".replace("o", 2)',
    '"foo bar".split(3)',
    '"foo".upper(7)',
])
def test_disallow_call(code):
    """
    Test that calls are disallowed.
    """
    with pytest.raises(CannotCall):
        code += '\nreturn "foo"'
        basic_displaylang_processor.process(code, {})
