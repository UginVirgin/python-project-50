import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("first_file", type=int)
    parser.add_argument("second_file", type=int)

    parser.add_argument(
            '-f', '--format',
            metavar='FORMAT',
            type=str,
            choices=['plain', 'json'],
            help='set format of output'
    )

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
