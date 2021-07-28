"""Find differences between two json or yaml files."""
import json
from collections import defaultdict
from os import path
from typing import Any, Dict

import yaml
from gendiff.formatters.stylish import is_child, stylish
from gendiff.key_states_constants import (
    ADDED,
    CHANGED_FROM,
    CHANGED_TO,
    REMOVED,
    SUBTREE,
    UNCHANGED,
    UPDATED,
)


def generate_diff(
    source_file_path: str,
    updated_file_path: str,
    formatter=stylish,
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
    source_file_data = parse_file_content(source_file_path)
    updated_file_data = parse_file_content(updated_file_path)
    diffs_tree = get_diffs_tree(source_file_data, updated_file_data)
    return formatter(diffs_tree)


def parse_file_content(file_path: str) -> Dict:
    """Convert content from JSON or YAML file.

    Args:
        file_path: path to file

    Returns:
        dictionary
    """
    _, extension = path.splitext(file_path)
    json_ext = '.json'
    yaml_ext = ('.yaml', '.yml')
    with open(file_path, 'r') as file_content:
        if extension == json_ext:
            return json.load(file_content)
        elif extension in yaml_ext:
            return yaml.safe_load(file_content)


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
        elif _has_subtree(source_file_data, updated_file_data, key):
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


def _has_subtree(source_file_data: Dict, updated_file_data: Dict, key: Any):
    return is_child(source_file_data.get(key)) and is_child(updated_file_data.get(key))  # noqa: E501
