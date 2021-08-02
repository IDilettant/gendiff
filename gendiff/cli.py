"""Shell parser module."""
from argparse import ArgumentParser

from gendiff.formatters.json_formatter import format_to_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish

FORMATS = {  # noqa: WPS407
    'stylish': stylish,
    'plain': plain,
    'json': format_to_json,
}
VERSION = '0.5.0'


def create_parser() -> ArgumentParser:
    """Create a parser instance able to parse args of script.

    return:
        Returns the parser instance
    """
    parser = ArgumentParser()
    parser.add_argument('first_file', help='path to JSON or YAML file')
    parser.add_argument('second_file', help='path to JSON or YAML file')
    parser.add_argument(
        '-f',
        '--format',
        choices=FORMATS.keys(),
        default='stylish',
        help='set format of output',
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='{prog} {version}'.format(prog=parser.prog, version=VERSION),
        help='print version info',
    )
    return parser
