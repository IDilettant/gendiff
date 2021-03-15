#!/usr/bin/env python

import argparse


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


def main():
    """Run module script."""
    parser = create_parser()
    args = parser.parse_args()
    print(args.first_file, args.second_file)


if __name__ == '__main__':
    main()
