#!/usr/bin/env python3
import argparse


def generate_diff():
    diff = argparse.ArgumentParser()
    parser.add_argument('first_file', help='')
    diff.add_argument('second_file', help='')
    diff.add_argument('-f', '--format', help='set format of output')
    return diff


def main():
    diff = generate_diff()
    namespace = diff.parse_args()
    print(namespace)


if __name__ == '__main__':
    main()