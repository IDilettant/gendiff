"""Formater module."""
import json
from typing import Any, Dict, List, Optional

IS_CHANGED = 'is changed'
IS_UNCHANGED = 'is unchanged'
IS_DELETED = 'is deleted'
IS_ADDED = 'is added'
HAS_CHILD_DIFF = 'has child diff'
CHILD_DIFF_REPR = 'child diff repr'
INDENT = ' ' * 4


def stylish(  # noqa: WPS210 WPS231 C901
    inter_repr: Dict,
    source1: Dict,
    source2: Dict,
    depth: int = 0,
) -> str:
    """Format internal representation of diffs to dictionary-like string.

    Args:
        inter_repr: registered result of compare between two files
        source1: file content
        source2: file content
        depth: level of nested

    Returns:
        representation of diffs to dictionary-like string
    """
    diffs = []
    indent = INDENT * depth
    for key, state in inter_repr.items():
        rendered_value_from_first = _render_as_string(
            source1.get(key),
            depth + 1,
        )
        rendered_value_from_second = _render_as_string(
            source2.get(key),
            depth + 1,
        )
        if state.get(HAS_CHILD_DIFF):  # noqa: WPS223
            diffs.append(
                '{0}    {1}: {2}'.format(
                    indent,
                    key,
                    stylish(
                        state[CHILD_DIFF_REPR],
                        source1[key],
                        source2[key],
                        depth + 1,
                    ),
                ),
            )
        elif state.get(IS_CHANGED):
            diffs.append('{0}  - {1}:{2}'.format(
                indent,
                key,
                rendered_value_from_first,
            ))
            diffs.append('{0}  + {1}:{2}'.format(
                indent,
                key,
                rendered_value_from_second,
            ))
        elif state.get(IS_UNCHANGED):
            diffs.append('{0}    {1}:{2}'.format(
                indent,
                key,
                rendered_value_from_first,
            ))
        elif state.get(IS_DELETED):
            diffs.append('{0}  - {1}:{2}'.format(
                indent,
                key,
                rendered_value_from_first,
            ))
        elif state.get(IS_ADDED):
            diffs.append('{0}  + {1}:{2}'.format(
                indent,
                key,
                rendered_value_from_second,
            ))
    return _format_to_dict_like(diffs, indent)


def is_child(key_value: Any):
    """Find out if an element is a child in a dictionary tree structure.

    Args:
        key_value: value of dictionary key

    Returns:
        bool
    """
    return isinstance(key_value, dict)


def _render_as_string(arg: Any, depth: int = 0) -> str:  # noqa: WPS231
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
        for key, dict_value in arg.items():
            dict_value = _render_as_string(dict_value, depth + 1)
            line = '{0}    {1}:{2}'.format(
                indent,
                key,
                dict_value,
            )
            lines.append(line)
        return ' {0}'.format(_format_to_dict_like(lines, indent))
    elif isinstance(arg, bool) or arg is None:
        return ' {0}'.format(json.dumps(arg))
    elif arg == '':
        return arg
    return ' {0}'.format(str(arg))


def _format_to_dict_like(lines: List, indent: Optional[str] = None):
    lines = '\n'.join(lines)
    return '{0}\n{1}\n{2}{3}'.format('{', lines, indent, '}')
