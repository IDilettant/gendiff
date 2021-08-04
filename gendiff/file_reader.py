"""Content parser module."""
import json
from os import path
from typing import Dict, TextIO

import yaml


def read_file(file_path: str):
    """Read JSON or YAML files.

    Args:
        file_path: path to file

    Returns:
        dictionary
    """
    file_content = _extract_file_content(file_path)
    extension = _get_extension(file_path)
    return _parse_file_content(file_content, extension)


def _parse_file_content(file_content: TextIO, extension: str) -> Dict:
    json_ext = '.json'
    yaml_ext = ('.yaml', '.yml')
    if extension == json_ext:
        return json.load(file_content)
    elif extension in yaml_ext:
        return yaml.safe_load(file_content)


def _extract_file_content(file_path: str) -> TextIO:
    file_path = path.abspath(file_path)
    with open(file_path, 'r') as file_content:
        return file_content


def _get_extension(file_path):
    return path.splitext(file_path)[1]
