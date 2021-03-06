"""Init package module."""
from gendiff.cli import create_parser
from gendiff.differ import get_diffs_tree
from gendiff.file_reader import read_file
from gendiff.formatters.json import format_to_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.scripts.gendiff import generate_diff

__all__ = (  # noqa: WPS410
    'create_parser',
    'stylish',
    'plain',
    'format_to_json',
    'generate_diff',
    'read_file',
    'get_diffs_tree',
)
