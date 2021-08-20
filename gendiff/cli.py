"""Shell parser module."""
from argparse import ArgumentParser

from gendiff.formatters.formats import FORMATS
from pkg_resources import get_distribution

BASE_FORMAT = 'stylish'


def create_parser() -> ArgumentParser:
    """Create a parser instance able to parse args of script.

    return:
        Returns the parser instance
    """
    parser = ArgumentParser()
    version = get_distribution('hexlet-code').version
    parser.add_argument('first_file', help='path to JSON or YAML file')
    parser.add_argument('second_file', help='path to JSON or YAML file')
    parser.add_argument(
        '-f',
        '--format',
        choices=FORMATS.keys(),
        default=BASE_FORMAT,
        help='set format of output',
    )
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='{prog} {version}'.format(prog=parser.prog, version=version),
        help='print version info',
    )
    return parser
