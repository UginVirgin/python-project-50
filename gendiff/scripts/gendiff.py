import argparse
import json
import os
from typing import Dict, Union


def generate_diff(file_path1, file_path2):
    with open(file_path1) as f1, open(file_path2) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
        return compare_diff(data1, data2)


def compare_diff(
        data1: Dict[str, Union[str, int, bool]],
        data2: Dict[str, Union[str, int, bool]]
) -> Dict: 
    
    data1_set = set(data1)
    data2_set = set(data2)
    union_set = data1_set | data2_set
    diff = {}

    for key in union_set:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                diff[key] = ("unchanged", data1[key])
            else:
                diff[key] = ("changed", data1[key], data2[key])
        elif key in data1 and key not in data2:
            diff[key] = ("deleted", data1[key])
        elif key not in data1 and key in data2:
            diff[key] = ("added", data2[key])
    return diff


def stylish(diff_dict) -> str:
    lines = ["{"]
    for key, value in diff_dict.items():
        status = value[0]
        if status == "unchanged":
            lines.append(f"    {key}: {value[1]}")
        elif status == "deleted":
            lines.append(f"  - {key}: {value[1]}")
        elif status == "added":
            lines.append(f"  + {key}: {value[1]}")
        elif status == "changed":
            old_value, new_value = value[1], value[2]
            lines.append(f"  - {key}: {old_value}")
            lines.append(f"  + {key}: {new_value}")
    lines.append("}")
    return "\n".join(lines)

        

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
            '-f', '--format',
            metavar='FORMAT',
            type=str,
            choices=['plain', 'json', "stylish"],
            help='set format of output'
    )

    args = parser.parse_args()
    path_to_file1 = args.first_file
    path_to_file2 = args.second_file
    diff = generate_diff(path_to_file1, path_to_file2)
    print(stylish(diff))





if __name__ == "__main__":
    main()
