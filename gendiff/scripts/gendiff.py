#!/usr/bin/env python
"""Main script module."""
from gendiff.cli import create_parser
from gendiff.differ import generate_diff


def main():
    """Run module script."""
    parser = create_parser()
    args = parser.parse_args()
    print(
        generate_diff(
            args.first_file,
            args.second_file,
            formatter=args.format,
        ),
    )


if __name__ == '__main__':
    main()
