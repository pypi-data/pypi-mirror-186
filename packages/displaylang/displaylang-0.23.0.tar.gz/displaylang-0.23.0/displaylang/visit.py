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


import ast


class DeleteNode:
    """
    Instances of this class may be returned by any "visit" method in a node
    visitor, in order to signal that the node should be deleted.

    We use this instead of None (as `ast.NodeTransformer` uses), since we
    sometimes actually want to return `None` as the value that should replace a
    node.
    """
    pass


class ExtendNode:
    """
    Instances of this class may be returned by any "visit" method in a node
    visitor, in order to signal that a list should be extended by all the
    values contained herein.

    We use this instead of a list (as `ast.NodeTransformer` uses), since we
    sometimes actually want to return a list as the value that should replace
    a node.
    """

    def __init__(self, values):
        self.values = values


def visitor_recurse(visitor, node, fields=None):
    """
    Visitor methods may start with a call to this method, in order
    to achieve a bottom-up traversal of the tree.

    fields: pass a set or list of field names to limit processing
        to these fields only.

    Compare `ast.NodeTransformer.generic_visit`.
    """
    for field, old_value in ast.iter_fields(node):
        if fields is None or field in fields:
            if isinstance(old_value, list):
                new_values = []
                for value in old_value:
                    if isinstance(value, ast.AST):
                        value = visitor.visit(value)
                        if isinstance(value, DeleteNode):
                            continue
                        elif isinstance(value, ExtendNode):
                            new_values.extend(value.values)
                            continue
                    new_values.append(value)
                old_value[:] = new_values
            elif isinstance(old_value, ast.AST):
                new_node = visitor.visit(old_value)
                if isinstance(new_node, DeleteNode):
                    delattr(node, field)
                else:
                    setattr(node, field, new_node)
    return node
