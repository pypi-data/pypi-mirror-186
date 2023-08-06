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

from displaylang.build import (
    process_displaylang, make_displaylang_processor,
)
from displaylang.depth import all_brackets_cumulative_depth
from displaylang.exceptions import ControlledEvaluationException
from displaylang.evaluate import ExpressionEvaluator, evaluate_expression


@pytest.mark.parametrize('code, expected', [
    ['{1:2, 3:4}', {1: 2, 3: 4}],
    ['[1, 2, 3]', [1, 2, 3]],
    ['(1, 2, 3)', (1, 2, 3)],
    ['{1, 2, 3}', {1, 2, 3}],
    ['[1, 2, 3, 4, 5][2]', 3],
    ['[1, 2, 3, 4, 5][2:4]', [3, 4]],
    ['[1, 2, 3, 4, 5][::-2]', [5, 3, 1]],
    ['{1:2, 3:4}[3]', 4],
    ['1 + 2', 3],
    ['1 - 2', -1],
    ['2 * 3', 6],
    ['3 / 2', 1.5],
    ['3 // 2', 1],
    ['11 % 7', 4],
    ['2**3', 8],
    ['7 << 1', 14],
    ['7 >> 1', 3],
    ['11 | 6', 15],
    ['11 ^ 6', 13],
    ['11 & 6', 2],
    ['+1', 1],
    ['-1', -1],
    ['not True', False],
    ['~5', -6],
    ['True and False', False],
    ['True or False', True],
    ['1 == 1', True],
    ['1 != 2', True],
    ['1 < 2 < 3', True],
    ['1 < 2 <= 2', True],
    ['3 > 2 > 1', True],
    ['2 >= 2 > 1', True],
    ['True is True', True],
    ['True is not False', True],
    ['3 in [2, 3, 5, 7]', True],
    ['4 not in [2, 3, 5, 7]', True],
])
def test_basic_expressions(code, expected):
    evaluator = ExpressionEvaluator()
    v = evaluate_expression(evaluator, code)
    assert v == expected


build_00 = """
s = 'foo'
t = s + 'bar'
return t
"""

build_01 = """
a = 2 + 3
b = a + 5
return str(b)
"""

build_02 = """
foo = [2*n 
    for n in [2, 3, 5, 7]]
return str(foo)
"""

build_03 = """
foo2 = [2*n+3*k for n, k in [(1, 2), (3, 4)]]
return str(foo2)
"""

build_04 = """
foo = [2*n for n in [2, 3, 5, 7] if n % 2 == 1]
return str(foo)
"""

build_05 = """
# This one demonstrates that names are not overwritten
# when they are used as bound vars in comprehensions.
n = 'bar'
foo = [2*n for n in [2, 3, 5, 7]]
return n
"""

build_06 = """
L = [2, 3, 5, 7, 11]
a = L[:2]
b = L[3:]
c = L[2:4]
d = L[1::2]
return str(a + b + c + d)
"""

build_07 = """
s = sum(n**2 for n in range(1, 8))
return str(s)
"""

build_08 = """
return str({n:n**2 for n in range(4)})
"""

build_09 = """
return str({n**2 for n in range(4)})
"""

build_10 = """
return f'{1+2} {3-4} {5*6} {10/8} {13//4} {14%5} {2**5} {7<<2} {7>>2} {12|10} {12^10} {12&10}'
"""

build_11 = """
return f'{+7} {-7} {not True} {~7} {True and False} {True or False}'
"""

build_12 = """
a = 1 if True else 2
a += 1
return str(a)
"""

build_13 = """
(a, [b, c]) = [f, g] = p = [1, (2, 3)]
return str(a + b + c + f + g[0] + g[1] + p[0])
"""

build_14 = """
# This involves an empty comprehension:
return str(['foo' for r in range(2, 2)])
"""


@pytest.mark.parametrize('code, s_exp, d_exp', [
    [build_00, 'foobar', {'s': 'foo', 't': 'foobar'}],
    [build_01, '10', {'a': 5, 'b': 10}],
    [build_02, '[4, 6, 10, 14]', {'foo': [4, 6, 10, 14]}],
    [build_03, '[8, 18]', {'foo2': [8, 18]}],
    [build_04, '[6, 10, 14]', {'foo': [6, 10, 14]}],
    [build_05, 'bar', {'n': 'bar', 'foo': [4, 6, 10, 14]}],
    [build_06, '[2, 3, 7, 11, 5, 7, 3, 7]', {'L': [2, 3, 5, 7, 11], 'a': [2, 3], 'b': [7, 11], 'c': [5, 7], 'd': [3, 7]}],
    [build_07, '140', {'s': 140}],
    [build_08, '{0: 0, 1: 1, 2: 4, 3: 9}', {}],
    [build_09, '{0, 1, 4, 9}', {}],
    [build_10, '3 -1 30 1.25 3 4 32 28 1 14 6 8', {}],
    [build_11, '7 -7 False -8 False True', {}],
    [build_12, '2', {'a': 2}],
    [build_13, '13', {'a': 1, 'b': 2, 'c': 3, 'f': 1, 'g': (2, 3), 'p': [1, (2, 3)]}],
    [build_14, '[]', {}],
])
def test_build(code, s_exp, d_exp):
    s, d = process_displaylang(code, {}, {}, [], add_builtins=True)
    interactive = False
    if interactive:
        print()
        print(s)
        print(d)
    assert s == s_exp
    assert d == d_exp


def test_build_with_fixed_processor():
    """
    Try using a fixed DisplayLangProcessor, to process multiple code strings.
    """
    cases = [
        [build_00, 'foobar', {'s': 'foo', 't': 'foobar'}],
        [build_01, '10', {'a': 5, 'b': 10}],
        [build_02, '[4, 6, 10, 14]', {'foo': [4, 6, 10, 14]}],
        [build_03, '[8, 18]', {'foo2': [8, 18]}],
        [build_04, '[6, 10, 14]', {'foo': [6, 10, 14]}],
        [build_05, 'bar', {'n': 'bar', 'foo': [4, 6, 10, 14]}],
        [build_06, '[2, 3, 7, 11, 5, 7, 3, 7]', {'L': [2, 3, 5, 7, 11], 'a': [2, 3], 'b': [7, 11], 'c': [5, 7], 'd': [3, 7]}],
        [build_07, '140', {'s': 140}],
        [build_08, '{0: 0, 1: 1, 2: 4, 3: 9}', {}],
        [build_09, '{0, 1, 4, 9}', {}],
        [build_10, '3 -1 30 1.25 3 4 32 28 1 14 6 8', {}],
        [build_11, '7 -7 False -8 False True', {}],
    ]
    dlp = make_displaylang_processor({}, [], add_builtins=True)
    for code, s_exp, d_exp in cases:
        s, d = dlp.process(code, {})
        interactive = False
        if interactive:
            print()
            print(s)
            print(d)
        assert s == s_exp
        assert d == d_exp


@pytest.mark.parametrize(['code', 'max_depth'], [
    ['a = [[[[[[[[ [[[[[[[[ [[[[[[[[ [[[[[[[[ [] ]]]]]]]] ]]]]]]]] ]]]]]]]] ]]]]]]]]', 33],
    ['a = [[[[[[[[ [[[[[[[[ [[[[[[[[ [[[[[[[[ [ "]]]]]" ] ]]]]]]]] ]]]]]]]] ]]]]]]]] ]]]]]]]]', 33],
    [r'a = [[[[[[[[ [[[[[[[[ [ "]]]]]\"" ] ]]]]]]]] ]]]]]]]]', 17],
    [r'a = [[[[[[[[ [[[[[[[[ [[ "\"[[[[[" ]] ]]]]]]]] ]]]]]]]]', 18],
    ['a = [[[[[[[[ [[[[[[[[ [ """]]]]]""" ] ]]]]]]]] ]]]]]]]]', 17],
    [r'a = [[[[[[[[ [[[[[[[[ [ """]]]]]""\"""" ] ]]]]]]]] ]]]]]]]]', 17],
    ['a = ([([([([{}])])])])', 9],
])
def test_all_brackets_cumulative_depth(code, max_depth):
    assert all_brackets_cumulative_depth(code) == max_depth


@pytest.mark.parametrize('code, err_msg', [
    # Can't format a float as an integer:
    ["f'{1.23:d}'", '''ValueError("Unknown format code 'd' for object of type 'float'")'''],
    # Can't do unpacking in an augmented assignment:
    ['a, b := 1, 2', '''Error parsing display widget build code.
invalid syntax (<unknown>, line 1)'''],
    # Can't assign to a set:
    ['{a, b, c} = {1, 2, 3}', '''Error parsing display widget build code.
cannot assign to set display (<unknown>, line 1)'''],
    # Failures to unpack:
    ['a, b = 1', '''Cannot unpack assignment.
At line 1, column 0.'''],
    ['a, (b, c) = 1, 2', '''Cannot unpack assignment.
At line 1, column 0.'''],
    # KeyError:
    ['{}[3]', 'KeyError(3)'],
])
def test_misc_errors(code, err_msg):
    code += '\nreturn "foo"'
    with pytest.raises(ControlledEvaluationException) as e:
        process_displaylang(code, {}, {}, [], add_builtins=True)
    assert str(e.value) == err_msg
