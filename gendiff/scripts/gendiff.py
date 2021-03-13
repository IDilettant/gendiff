#!/usr/bin/env python3
import argparse


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    return parser


def main():
    parser = create_parser()
    namespace = parser.parse_args()
    print(namespace)


if __name__ == '__main__':
    main()