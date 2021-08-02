"""Content parser module."""
import json
from os import path
from typing import Dict, TextIO

import yaml


def extract_file_content(file_path: str) -> Dict:
    """Convert content from JSON or YAML file.

    Args:
        file_path: path to file

    Returns:
        dictionary
    """
    _, extension = path.splitext(file_path)
    with open(file_path, 'r') as file_content:
        return _parse_file_content(file_content, extension)


def _parse_file_content(file_content: TextIO, extension: str) -> Dict:
    json_ext = '.json'
    yaml_ext = ('.yaml', '.yml')
    if extension == json_ext:
        return json.load(file_content)
    elif extension in yaml_ext:
        return yaml.safe_load(file_content)
