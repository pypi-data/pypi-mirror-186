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

from typing import (
    Any, Iterable, List, Tuple, Dict, Sequence, Optional as o, Union as u
)
from .allow import (
    ArgSpec as a,
    AllowedCallable as c,
    StrPermType as s,
    Tail as t
)

# As the language evolves, we expect the lists of allowed callables to grow.

# The "basic callables" are the ones that will be added to your `basic_vars`
# in `process_displaylang()` if you set `add_builtins=True` there. They will
# also be added to the set of allowed callables in this case.
basic_callables = [
    c(len, [
        [Iterable],
        [s.ANY],
    ]),
    c(range, [t(int)]),
    c(str, [Any]),
    c(sum, [
        [Sequence],
        [Sequence, Any],
    ]),
    c(zip, [t(Iterable)]),
]

# While the "other callables" will not be added to `basic_vars`, they will be
# added to the set of allowed callables when you set `add_builtins=True`
# in `process_displaylang()`.
other_callables = [
    c(list.append, [Any], method_of=list),
    c(list.extend, [Sequence], method_of=list),

    c(str.join, [Sequence[str]], method_of=s.ANY),
    c(str.lower, [], method_of=s.ANY),
    c(str.replace, [s.ANY, s.ANY], method_of=s.ANY),
    c(str.split, [
        [],
        [s.ANY]
    ], method_of=s.ANY),
    c(str.upper, [], method_of=s.ANY),
]
