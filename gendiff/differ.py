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
    source_file_path: str,
    updated_file_path: str,
    formatter: str = 'stylish',
) -> str:
    """Find differences between two files.

    Perform result of search as string in dictionary like format

    Args:
        source_file_path: path to file
        updated_file_path: path to file
        formatter: function for format to dictionary-like string

    Returns:
        Diffs in dictionary like format
    """
    source_file_data = read_file(source_file_path)
    updated_file_data = read_file(updated_file_path)
    diffs_tree = get_diffs_tree(source_file_data, updated_file_data)
    return FORMATS[formatter](diffs_tree)


def get_diffs_tree(  # noqa: WPS210 WPS231 C901
    source_file_data: Dict,
    updated_file_data: Dict,
) -> Dict:
    """Get internal representation of differences between two dictionaries.

    Args:
        source_file_data: file content
        updated_file_data: file content

    Returns:
        registered result of compare between two files
    """
    only_first = set(source_file_data) - set(updated_file_data)
    only_second = set(updated_file_data) - set(source_file_data)
    common_keys = sorted(source_file_data.keys() | updated_file_data.keys())
    diffs_tree = defaultdict(dict)
    for key in common_keys:
        source_value = source_file_data.get(key)
        new_value = updated_file_data.get(key)
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
