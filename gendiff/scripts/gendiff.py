#!/usr/bin/env python
"""Finds differences between two json files.

Displays them on the screen in detail as a string.
"""
import argparse
import json


def create_parser():
    """Create a parser instance able to parse args of script.

    return:
        Returns the parser instance
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument('-f', '--format', help='set format of output')
    return parser


def decode(json_source):
    """Decode text file containing a JSON document into a Python object.

    Args:
        json_source: text file

    Returns:
        The Python object
    """
    with open(json_source, 'r') as source:
        return json.load(source)


def main():
    """Run module script."""
    parser = create_parser()
    args = parser.parse_args()
    print(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
