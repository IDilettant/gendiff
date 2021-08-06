"""Content parser module."""
from os import path
from typing import Dict

from gendiff.parser import parse_file_content


def read_file(file_path: str) -> Dict:
    """Read JSON or YAML files.

    Args:
        file_path: path to file

    Returns:
        converted dictionary-like file content
    """
    file_content = _extract_file_content(file_path)
    extension = _get_extension(file_path)
    return parse_file_content(file_content, extension)


def _extract_file_content(file_path: str) -> str:
    file_path = path.abspath(file_path)
    with open(file_path, 'r') as file_content:
        return file_content.read()


def _get_extension(file_path):
    return path.splitext(file_path)[1]
