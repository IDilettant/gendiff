"""Shell parser module."""
from argparse import ArgumentParser

from gendiff.formatters.json import format_to_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from pkg_resources import get_distribution

FORMATS = {  # noqa: WPS407
    'stylish': stylish,
    'plain': plain,
    'json': format_to_json,
}
VERSION = get_distribution('hexlet-code').version


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
