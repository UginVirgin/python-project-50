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


def generate_diff(file_path1, file_path2, formatter="stylish"):
    data1 = parser(file_path1)
    data2 = parser(file_path2)
    diff = find_diff(data1, data2)
    if isinstance(formatter, str):
        formatter = formatters[formatter]
    diff = formatter(diff)

    return diff
