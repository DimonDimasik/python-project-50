#!/usr/bin/env python3
import argparse
from gendiff.scripts.generate_diff import generate_diff


def parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        help='set format of output')
    return parser.parse_args()


def main():
    args = parse()
    print(generate_diff(args.first_file, args.second_file, format_name=args.format))


if __name__ == '__main__':
    main()
