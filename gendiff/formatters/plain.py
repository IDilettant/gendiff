"""Plain formatter module."""
from typing import Any, Dict

from gendiff.inter_repr import (
    ADDED,
    CHANGED_FROM,
    CHANGED_TO,
    REMOVED,
    SUBTREE,
    UPDATED,
)

BOOL_TRUE = 'true'
BOOL_FALSE = 'false'
NONE = 'null'


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
    for key, node in sorted(diffs_tree.items()):
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


def _render_as_string(arg: Any) -> str:  # noqa: WPS212
    """Render as string representation.

    Args:
        arg: some value

    Returns:
        string for plain format representation
    """
    if isinstance(arg, (dict, list, tuple, set)):
        return '[complex value]'
    if arg is True:
        return BOOL_TRUE
    if arg is False:
        return BOOL_FALSE
    if arg is None:
        return NONE
    if isinstance(arg, (int, float)):
        return '{0}'.format(str(arg))
    return "'{0}'".format(str(arg))
