import argparse
from .parser import parser
from .find_diff import find_diff
from gendiff.formatters.json_formatter import json_formatter
from gendiff.formatters.plain_formatter import plain_formatter
from gendiff.formatters.stylish_formatter import stylish





formatters = {
    "json": json_formatter,
    "plain": plain_formatter,
    "stylish": stylish
}


def generate_diff(file_path1, file_path2, formatter="json"):
    data1 = parser(file_path1)
    data2 = parser(file_path2)
    diff = find_diff(data1, data2)
    # print(diff)    # ------------ОТЛАДОЧНЫЙ ПРИНТ--------------
    if isinstance(formatter, str):
        formatter = formatters[formatter]
    diff = formatter(diff)

    return diff


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
            '-f', '--format',
            metavar='FORMAT',
            type=str,
            choices=['plain', 'json', "stylish"],
            help='set format of output',
            default="json"
    )

    args = parser.parse_args()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    formatter = args.format
    diff = generate_diff(path_to_file1, path_to_file2, formatter)
    print(diff)



if __name__ == "__main__":
    main()
