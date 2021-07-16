#!/usr/bin/env python
"""Find differences between two json files.

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


def decode(file_path):
    """Decode text file containing a JSON document into a Python object.

    Args:
        file_path: JSON-file

    Returns:
        Dictionary
    """
    with open(file_path, 'r') as json_content:
        return json.load(json_content)


def get_diffs(source1, source2):
    """Find differences between two dictionaries.

    Args:
        source1 (dict): arg content
        source2 (dict): arg content

    Returns:
        Diffs
    """
    keys = sorted(source1.keys() | source2.keys())
    only_first = set(source1) - set(source2)
    first_and_second = set(source1) & set(source2)
    diffs = []
    for key in keys:
        if key in first_and_second:
            if source1[key] == source2[key]:
                diffs.append('    {0}: {1}'.format(key, source1[key]))
            else:
                diffs.append('  - {0}: {1}'.format(key, source1[key]))
                diffs.append('  + {0}: {1}'.format(key, source2[key]))
        elif key in only_first:
            diffs.append('  - {0}: {1}'.format(key, source1[key]))
        else:
            diffs.append('  + {0}: {1}'.format(key, source2[key]))
    return diffs


def render_as_string(diffs):
    """Render diffs as string representation in dictionary like format.

    Args:
        diffs (list): strings with differences between two dictionaries

    Returns:
        Diffs in dictionary like format
    """
    diffs = '\n'.join(diffs)
    return '{0}\n{1}\n{2}'.format('{', diffs, '}')


def generate_diff(source1, source2):
    """Find differences between two JSON files.

    Perform result of search as string in dictionary like format

    Args:
        source1: JSON-file
        source2: JSON-file

    Returns:
        Diffs in dictionary like format
    """
    source1 = decode(source1)
    source2 = decode(source2)
    diffs = get_diffs(source1, source2)
    return render_as_string(diffs)


def main():
    """Run module script."""
    parser = create_parser()
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':
    main()
