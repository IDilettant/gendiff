"""Stylish formatter module."""
import json
from typing import Any, Dict, List, Optional

from gendiff.key_states_constants import (
    ADDED,
    CHANGED_FROM,
    CHANGED_TO,
    REMOVED,
    SUBTREE,
    UNCHANGED,
    UPDATED,
)

INDENT = ' ' * 4


def stylish(  # noqa: WPS210 WPS231 C901
    diffs_tree: Dict,
    depth: int = 0,
) -> str:
    """Format internal representation of diffs to dictionary-like string.

    Args:
        diffs_tree: registered result of compare between two files
        depth: level of nested

    Returns:
        representation of diffs to dictionary-like string
    """
    diffs = []
    indent = INDENT * depth
    for key, node in diffs_tree.items():
        node_value = _render_to_string(node.get('value'), depth + 1)
        node_state = node.get('state')
        if node_state == SUBTREE:  # noqa: WPS223
            diffs.append(
                '{indent}    {key}: {value}'.format(
                    indent=indent,
                    key=key,
                    value=stylish(
                        node['children_diff'],
                        depth + 1,
                    ),
                ),
            )
        elif node_state == UPDATED:
            diffs.append(
                '{indent}  - {key}: {value}'.format(
                    indent=indent,
                    key=key,
                    value=_render_to_string(
                        node['value'][CHANGED_FROM],
                        depth + 1,
                    ),
                ),
            )
            diffs.append(
                '{indent}  + {key}: {value}'.format(
                    indent=indent,
                    key=key,
                    value=_render_to_string(
                        node['value'][CHANGED_TO],
                        depth + 1,
                    ),
                ),
            )
        elif node_state == UNCHANGED:
            diffs.append(
                '{indent}    {key}: {value}'.format(
                    indent=indent,
                    key=key,
                    value=node_value,
                ),
            )
        elif node_state == REMOVED:
            diffs.append(
                '{indent}  - {key}: {value}'.format(
                    indent=indent,
                    key=key,
                    value=node_value,
                ),
            )
        elif node_state == ADDED:
            diffs.append(
                '{indent}  + {key}: {value}'.format(
                    indent=indent,
                    key=key,
                    value=node_value,
                ),
            )
    return _format_to_dict_like(diffs, indent)


def is_child(key_value: Any) -> bool:
    """Find out if an element is a child in a dictionary tree structure.

    Args:
        key_value: value of dictionary key

    Returns:
        bool
    """
    return isinstance(key_value, dict)


def _render_to_string(arg: Any, depth: int = 0) -> str:  # noqa: WPS231
    """Render as string representation.

    If argument is dictionary or list render in dictionary-like format.

    Args:
        arg: some value
        depth: level of nested

    Returns:
        dictionary-like format representation
    """
    indent = INDENT * depth
    if is_child(arg):
        lines = []
        for key, node_value in arg.items():
            node_value = _render_to_string(node_value, depth + 1)
            line = '{indent}    {key}: {value}'.format(
                indent=indent,
                key=key,
                value=node_value,
            )
            lines.append(line)
        return _format_to_dict_like(lines, indent)
    elif isinstance(arg, bool) or arg is None:
        return json.dumps(arg)
    elif arg == '':
        return arg
    return str(arg)


def _format_to_dict_like(lines: List, indent: Optional[str] = None) -> str:
    lines = '\n'.join(lines)
    return '{0}\n{1}\n{2}{3}'.format('{', lines, indent, '}')
