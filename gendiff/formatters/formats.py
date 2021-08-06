"""Formats module."""
from gendiff.formatters.json import format_to_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish

FORMATS = {  # noqa: WPS407
    'stylish': stylish,
    'plain': plain,
    'json': format_to_json,
}
