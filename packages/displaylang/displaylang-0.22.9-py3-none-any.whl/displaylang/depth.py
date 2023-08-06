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

import sys

from .exceptions import ControlledEvaluationException
from pfsc_util.scan import PythonModuleStringAwareScanner


HALF_RECURSION_LIMIT = sys.getrecursionlimit() // 2


class BracketDepthScanner(PythonModuleStringAwareScanner):
    """
    Computes the deepest nesting depth in a string of Python code, across all
    three bracket types () [] {}, with all three types contributing to a single
    count. For example, after "([{" the depth is 3.

    We ignore brackets occurring within Python strings.
    """

    def __init__(self):
        super().__init__()
        self.max_depth = 0
        self.cur_depth = 0
        self.next_close = None
        self.pairs = {"(": ")", "[": "]", "{": "}"}

    def state_0(self, c, i):
        if c in "([{":
            self.cur_depth += 1
            self.max_depth = max(self.max_depth, self.cur_depth)
            self.next_close = self.pairs.get(c)
        elif c == self.next_close:
            self.cur_depth = max(0, self.cur_depth - 1)
        return None, None


def all_brackets_cumulative_depth(raw_text):
    """
    Compute the deepest nesting depth in a string of Python code, across all
    three bracket types () [] {}, with all three types contributing to a single
    count. For example, after "([{" the depth is 3.

    We ignore brackets occurring within Python strings.
    """
    bds = BracketDepthScanner()
    bds.scan(raw_text)
    return bds.max_depth


def check_displaylang_dims(raw_text, max_len=0, max_depth=-1):
    """
    Check that a string is not too long or too deep (in parenthesis nesting),
    for safe parsing as displaylang.

    @param raw_text: the string to be checked.
    @param max_len: int
        The maximum allowed length for the code.
        If 0 (the default), no max length is imposed.
    @param max_depth: int
        The maximum allowed bracket depth for the code.
        If 0, no max depth is imposed.
        If -1 (the default), we use half of ``sys.getrecursionlimit()``, i.e.
        half the maximum depth of the Python interpreter stack.
    @return: nothing
    @raise: ControlledEvaluationException if given text is too long, or has
    too deep bracket nesting.
    """
    if 0 < max_len < len(raw_text):
        raise ControlledEvaluationException("DisplayLang code too long.")
    if max_depth == -1:
        max_depth = HALF_RECURSION_LIMIT
    if 0 < max_depth < all_brackets_cumulative_depth(raw_text):
        raise ControlledEvaluationException("DisplayLang code too deep.")
