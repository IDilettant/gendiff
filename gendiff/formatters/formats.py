"""Formats module."""
from gendiff.formatters.json import format_to_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish

STYLISH = 'stylish'
PLAIN = 'plain'
JSON = 'json'
FORMATS = {  # noqa: WPS407
    STYLISH: stylish,
    PLAIN: plain,
    JSON: format_to_json,
}
