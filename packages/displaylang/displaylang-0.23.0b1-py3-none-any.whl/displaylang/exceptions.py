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


"""Exceptions for parsing. """


class ControlledEvaluationException(Exception):
    """Any exception during use of a ControlledEvaluator. """
    pass


class BadArgs(ControlledEvaluationException):
    """
    Represents a failure of given positional and keyword args to match a
    particular Signature for an AllowedCallable.
    """
    pass


class CannotCall(ControlledEvaluationException):
    """
    Represents a failure to call an AllowedCallable `ac`, meaning every
    Signautre raised a `BadArgs` exception.

    Stores a list of `BadArgs` exceptions, one for each alternative Signature
    of `ac`.
    """

    def __init__(self, badArgsExceps):
        self.badArgsExceps = badArgsExceps

    def __str__(self):
        return '\n'.join(str(e) for e in self.badArgsExceps)


class DisallowedCallable(ControlledEvaluationException):
    """
    This means a call was rejected, not due to any issue with the arguments,
    but simply because the callable itself is not allowed at all.
    """
    pass
