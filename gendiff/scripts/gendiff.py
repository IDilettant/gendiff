#!/usr/bin/env python
"""Find differences between two json files.

Displays them on the screen in detail as a string.
"""
import json
from collections import defaultdict
from os import path
from typing import Any, Dict

import yaml
from gendiff.scripts.shell_parser import create_parser
from gendiff.scripts.stylish import (
    CHILDREN_DIFF_REPR,
    HAS_CHILD_UPDATES,
    IS_ADDED,
    IS_CHANGED,
    IS_DELETED,
    IS_UNCHANGED,
    is_child,
    stylish,
)


def generate_diff(source1: str, source2: str, formatter=stylish) -> str:
    """Find differences between two JSON files.

    Perform result of search as string in dictionary like format

    Args:
        source1: path to JSON-file
        source2: path to JSON-file
        formatter: function for format to dictionary-like string

    Returns:
        Diffs in dictionary like format
    """
    source1 = convert_file_content(source1)
    source2 = convert_file_content(source2)
    diffs_repr = get_diffs_repr(source1, source2)
    return formatter(diffs_repr, source1, source2)


def convert_file_content(file_path: str) -> Dict:
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


def get_diffs_repr(source1: Dict, source2: Dict) -> Dict:  # noqa: WPS231
    """Get internal representation of differences between two dictionaries.

    Args:
        source1: file content
        source2: file content

    Returns:
        registered result of compare between two files
    """
    only_first = set(source1) - set(source2)
    only_second = set(source2) - set(source1)
    both_sources = set(source1) & set(source2)
    inter_repr = defaultdict(dict)
    for key in sorted(source1.keys() | source2.keys()):
        if key in both_sources:
            inter_repr[key][IS_CHANGED] = source1[key] != source2[key]
            inter_repr[key][IS_UNCHANGED] = source1[key] == source2[key]
        elif key in only_first:
            inter_repr[key][IS_DELETED] = True
        elif key in only_second:
            inter_repr[key][IS_ADDED] = True
        if is_child(source1.get(key)) and is_child(source2.get(key)):
            _register_children(source1, source2, inter_repr, key)
    return inter_repr


def _register_children(
    source1: Dict,
    source2: Dict,
    inter_repr: Dict,
    key: Any,
):
    """Compare sources and register diffs.

    Args:
        source1: file content
        source2: file content
        inter_repr: registered result of compare between two files
        key: the key contained in both dictionaries
    """
    state = inter_repr[key]
    state[IS_CHANGED] = False
    state[IS_UNCHANGED] = True
    state[HAS_CHILD_UPDATES] = True
    state[CHILDREN_DIFF_REPR] = get_diffs_repr(source1[key], source2[key])


def main():
    """Run module script."""
    parser = create_parser()
    args = parser.parse_args()
    print(
        generate_diff(
            args.first_file,
            args.second_file,
            formatter=args.format,
        ),
    )


if __name__ == '__main__':
    main()
