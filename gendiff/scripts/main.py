import argparse
from gendiff.scripts.gendiff import generate_diff


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
            default="stylish"
    )

    args = parser.parse_args()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    formatter = args.format
    diff = generate_diff(path_to_file1, path_to_file2, formatter)
    print(diff)


if __name__ == "__main__":
    main()