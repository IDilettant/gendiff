"""Find differences between two json or yaml files."""
from collections import defaultdict
from typing import Any, Dict

from gendiff.file_reader import read_file
from gendiff.formatters.formats import FORMATS

UPDATED = 'updated'
CHANGED_FROM = 'changed from'
CHANGED_TO = 'changed to'
UNCHANGED = 'unchanged'
REMOVED = 'removed'
ADDED = 'added'
SUBTREE = 'subtree'
CHILDREN_DIFF = 'children_diff'


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
    return FORMATS[formatter](diffs_tree)  # type: ignore


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
    only_first = first_file_data.keys() - second_file_data.keys()
    only_second = second_file_data.keys() - first_file_data.keys()
    common_keys = first_file_data.keys() & second_file_data.keys()
    diffs_tree: Dict = defaultdict(dict)
    for key in only_first:
        source_value = first_file_data[key]
        diffs_tree[key].update(state=REMOVED, value=source_value)  # noqa: WPS204 E501
    for key in only_second:  # noqa: WPS440
        new_value = second_file_data[key]
        diffs_tree[key].update(state=ADDED, value=new_value)
    for key in common_keys:  # noqa: WPS440
        source_value = first_file_data[key]
        new_value = second_file_data[key]
        if source_value == new_value:
            diffs_tree[key].update(
                state=UNCHANGED,
                value=source_value,
            )
        elif _has_subtree_diff(source_value, new_value):
            diffs_tree[key].update(
                state=SUBTREE,
                children_diff=get_diffs_tree(source_value, new_value),  # type: ignore  # noqa: E501
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
