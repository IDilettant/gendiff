"""Find differences between two json or yaml files."""
from collections import defaultdict
from typing import Any, Dict

from gendiff.constants import (
    ADDED,
    CHANGED_FROM,
    CHANGED_TO,
    REMOVED,
    SUBTREE,
    UNCHANGED,
    UPDATED,
)
from gendiff.file_reader import read_file
from gendiff.formatters.formats import FORMATS


def generate_diff(
    first_file_path: str,
    second_file_path: str,
    formatter: str = 'stylish',
) -> str:
    """Find differences between two files.

    Perform result of search as string in dictionary like format

    Args:
        first_file_path: path to file
        second_file_path: path to file
        formatter: function for format to dictionary-like string

    Returns:
        Diffs in dictionary like format
    """
    first_file_data = read_file(first_file_path)
    second_file_data = read_file(second_file_path)
    diffs_tree = get_diffs_tree(first_file_data, second_file_data)
    return FORMATS[formatter](diffs_tree)


def get_diffs_tree(  # noqa: WPS210 WPS231 C901
    first_file_data: Dict,
    second_file_data: Dict,
) -> Dict:
    """Get internal representation of differences between two dictionaries.

    Args:
        first_file_data: file content
        second_file_data: file content

    Returns:
        registered result of compare between two files
    """
    only_first = set(first_file_data) - set(second_file_data)
    only_second = set(second_file_data) - set(first_file_data)
    common_keys = sorted(first_file_data.keys() | second_file_data.keys())
    diffs_tree = defaultdict(dict)
    for key in common_keys:
        source_value = first_file_data.get(key)
        new_value = second_file_data.get(key)
        if key in only_first:  # noqa: WPS223
            diffs_tree[key].update(state=REMOVED, value=source_value)  # noqa: WPS204 E501
        elif key in only_second:
            diffs_tree[key].update(state=ADDED, value=new_value)
        elif source_value == new_value:
            diffs_tree[key].update(
                state=UNCHANGED,
                value=source_value,
            )
        elif _has_subtree_diff(source_value, new_value):
            diffs_tree[key].update(
                state=SUBTREE,
                children_diff=get_diffs_tree(source_value, new_value),
            )
        elif source_value != new_value:
            diffs_tree[key].update(
                state=UPDATED,
                value={CHANGED_FROM: source_value, CHANGED_TO: new_value},
            )
    return diffs_tree


def _has_subtree_diff(
    source_value: Any,
    new_value: Any,
) -> bool:
    return isinstance(source_value, dict) and isinstance(new_value, dict)
