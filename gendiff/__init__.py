"""Init package module."""
from gendiff.differ import get_diffs_tree, parse_file_content
from gendiff.formatters.json_formatter import format_to_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.scripts.gendiff import generate_diff
from gendiff.shell_parser import create_parser

__all__ = (  # noqa: WPS410
    'create_parser',
    'stylish',
    'plain',
    'format_to_json',
    'generate_diff',
    'parse_file_content',
    'get_diffs_tree',
)
