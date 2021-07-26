"""Plain formatter module."""
import json
from typing import Any, Dict

from gendiff.scripts.stylish import (
    CHILDREN_DIFF_REPR,
    HAS_CHILD_UPDATES,
    IS_ADDED,
    IS_CHANGED,
    IS_DELETED,
    is_child,
)


def plain(  # noqa: WPS210 WPS231
    inter_repr: Dict,
    source1: Dict,
    source2: Dict,
    path_to_value: str = '',
):
    """Format internal representation of diffs to plain string.

    Args:
        inter_repr: registered result of compare between two files
        source1: file content
        source2: file content
        path_to_value: path by keys to value in dictionary

    Returns:
        representation of diffs to plain string
    """
    diffs = []
    for key, state in inter_repr.items():
        sub_path_to_value = '{0}.{1}'.format(
            path_to_value,
            str(key),
        ) if path_to_value else str(key)
        source_value = _render_as_string(source1.get(key))
        new_value = _render_as_string(source2.get(key))
        if state.get(HAS_CHILD_UPDATES):
            diff = plain(
                state[CHILDREN_DIFF_REPR],
                source1[key],
                source2[key],
                sub_path_to_value,
            )
            diffs.append(diff)
        elif state.get(IS_CHANGED):
            diff = "Property '{0}' was updated. From {1} to {2}".format(
                sub_path_to_value,
                source_value,
                new_value,
            )
            diffs.append(diff)
        elif state.get(IS_DELETED):
            diff = "Property '{0}' was removed".format(sub_path_to_value)
            diffs.append(diff)
        elif state.get(IS_ADDED):
            diff = "Property '{0}' was added with value: {1}".format(
                sub_path_to_value,
                new_value,
            )
            diffs.append(diff)
    return '\n'.join(diffs)


def _render_as_string(arg: Any) -> str:
    """Render as string representation.

    Args:
        arg: some value

    Returns:
        string for plain format representation
    """
    if any([  # noqa: WPS337
        is_child(arg),
        isinstance(arg, list),
        isinstance(arg, tuple),
        isinstance(arg, set),
    ]):
        return '[complex value]'
    elif isinstance(arg, bool) or arg is None:
        return json.dumps(arg)
    return "'{0}'".format(str(arg))
