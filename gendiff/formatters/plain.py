"""Plain formatter module."""
import json
from typing import Any, Dict

from gendiff.diff_sorter import sort_with_abc_order
from gendiff.inter_repr import (
    ADDED,
    CHANGED_FROM,
    CHANGED_TO,
    REMOVED,
    SUBTREE,
    UPDATED,
)


def plain(  # noqa: WPS210 WPS231
    diffs_tree: Dict,
    path_to_value: str = '',
) -> str:
    """Format internal representation of diffs to plain string.

    Args:
        diffs_tree: registered result of compare between two files
        path_to_value: path by keys to value in dictionary

    Returns:
        representation of diffs to plain string
    """
    diffs = []
    for key, node in sort_with_abc_order(diffs_tree).items():
        node_value = _render_as_string(node.get('value'))
        node_state = node.get('state')
        sub_path_to_value = '{path}.{key}'.format(
            path=path_to_value,
            key=str(key),
        ) if path_to_value else str(key)
        if node_state == SUBTREE:
            diffs.append(
                plain(
                    node['children_diff'],
                    sub_path_to_value,
                ),
            )
        elif node_state == UPDATED:
            diffs.append(
                "Property '{key}' was updated. From {old} to {new}".format(
                    key=sub_path_to_value,
                    old=_render_as_string(node['value'][CHANGED_FROM]),
                    new=_render_as_string(node['value'][CHANGED_TO]),
                ),
            )

        elif node_state == REMOVED:
            diffs.append(
                "Property '{key}' was removed".format(key=sub_path_to_value),
            )
        elif node_state == ADDED:
            diffs.append(
                "Property '{key}' was added with value: {value}".format(
                    key=sub_path_to_value,
                    value=node_value,
                ),
            )
    return '\n'.join(diffs)


def _render_as_string(arg: Any) -> str:
    """Render as string representation.

    Args:
        arg: some value

    Returns:
        string for plain format representation
    """
    if any([  # noqa: WPS337
        isinstance(arg, dict),
        isinstance(arg, list),
        isinstance(arg, tuple),
        isinstance(arg, set),
    ]):
        return '[complex value]'
    elif isinstance(arg, bool) or arg is None:
        return json.dumps(arg)
    elif isinstance(arg, (int, float)):
        return str(arg)
    return "'{0}'".format(str(arg))
