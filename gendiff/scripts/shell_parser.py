"""Shell parser module."""
from argparse import ArgumentParser

from gendiff.scripts.stylish import stylish


def create_parser() -> ArgumentParser:
    """Create a parser instance able to parse args of script.

    return:
        Returns the parser instance
    """
    parser = ArgumentParser()
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument(
        '-f',
        '--format',
        default=stylish,
        help='set format of output',
    )
    return parser
