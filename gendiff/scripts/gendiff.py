#!/usr/bin/env python
"""Main script module."""
from gendiff.differ import generate_diff
from gendiff.shell_parser import FORMATTERS, create_parser


def main():
    """Run module script."""
    parser = create_parser()
    args = parser.parse_args()
    print(
        generate_diff(
            args.first_file,
            args.second_file,
            formatter=FORMATTERS.get(args.format),
        ),
    )


if __name__ == '__main__':
    main()
