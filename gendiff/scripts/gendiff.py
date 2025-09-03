import argparse


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("first_file", type=int, help="first_argument")
    parser.add_argument("second_file", type=int, help="second_argument")

    args = parser.parse_args()
    print(args)


if __name__ == "__main__":
    main()
