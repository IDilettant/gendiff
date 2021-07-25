"""Init package module."""
from gendiff.scripts.gendiff import (
    convert_file_content,
    generate_diff,
    get_diffs_repr,
)
from gendiff.scripts.shell_parser import create_parser
from gendiff.scripts.stylish import stylish

__all__ = (  # noqa: WPS410
    'create_parser',
    'stylish',
    'generate_diff',
    'convert_file_content',
    'get_diffs_repr',
)
