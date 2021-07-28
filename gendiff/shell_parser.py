"""Shell parser module."""
from argparse import ArgumentParser

from gendiff.scripts.gendiff import FORMATTERS


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
        choices=FORMATTERS.keys(),
        default='stylish',
        help='set format of output (stylish by default)',
    )
    # parser.add_argument(
    #     '-v', '--version',
    #     action='version',
    #     version='%(prog)s 0.10.2',
    # )
    return parser
