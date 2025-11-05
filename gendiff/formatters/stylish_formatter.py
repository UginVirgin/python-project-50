def stylish(diff):
    result = '{\n' + stylish_formatter(diff) + '\n}'
    return result


def stylish_formatter(diff, depth=1):
    lines = []
    for key, (type, value) in sorted(diff.items()):
        lines = add_new_line(lines, key, value, depth, type)
    result = '\n'.join(lines)
    return result


def add_new_line(lines, key, value, depth, type):
    prefix = '  '
    if type == 'nested':
        indent = (4 * depth - 2) * ' '
        child_diff = stylish_formatter(value, depth + 1)
        formated_value = f'{{\n{child_diff}\n{indent}  }}'
        lines = add_indent_and_format(depth, lines, prefix, key, formated_value)
    elif type == 'changed':
        lines = changed_data_diff(lines, value, depth, key)
    elif type == 'added':
        prefix = '+ '
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    elif type == 'removed':
        prefix = '- '
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    else:
        lines = add_indent_and_format(depth, lines, prefix, key, value)
    return lines


def add_indent_and_format(depth, lines, prefix, key, value):
    formated_value = format_value(value, depth + 1)
    indent = (4 * depth - 2) * ' '
    lines.append(f"{indent}{prefix}{key}: {formated_value}")
    return lines


def format_value(value, depth):
    if isinstance(value, dict):
        prefix = '  '
        lines = ['{']
        for key, val in value.items():
            formated_value = format_value(val, depth + 1)
            lines = add_indent_and_format(depth, lines,
                                          prefix, key, formated_value)
        indent = ' ' * (4 * (depth - 1))
        lines.append(f"{indent}}}")
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    return str(value)


def changed_data_diff(lines, value, depth, key):
    old, new = value
    old_new_pairs = [('- ', old), ('+ ', new)]
    for prefix, value in old_new_pairs:
        formated_value = format_value(value, depth + 1)
        lines = add_indent_and_format(depth, lines, prefix, key, formated_value)
    return lines

# STYLISH RESULT
# {
#     common: {
#       + follow: false
#         setting1: Value 1
#       - setting2: 200
#       - setting3: true
#       + setting3: null
#       + setting4: blah blah
#       + setting5: {
#             key5: value5
#         }
#         setting6: {
#             doge: {
#               - wow: 
#               + wow: so much
#             }
#             key: value
#           + ops: vops
#         }
#     }
#     group1: {
#       - baz: bas
#       + baz: bars
#         foo: bar
#       - nest: {
#             key: value
#         }
#       + nest: str
#     }
#   - group2: {
#         abc: 12345
#         deep: {
#             id: 45
#         }
#     }
#   + group3: {
#         deep: {
#             id: {
#                 number: 45
#             }
#         }
#         fee: 100500
#     }
# }

# diff
# {
#   "common": [
#     "nested",
#     {
#       "follow": [
#         "added",
#         false
#       ],
#       "setting1": [
#         "unchanged",
#         "Value 1"
#       ],
#       "setting2": [
#         "removed",
#         200
#       ],
#       "setting3": [
#         "changed",
#         [
#           true,
#           null
#         ]
#       ],
#       "setting4": [
#         "added",
#         "blah blah"
#       ],
#       "setting5": [
#         "added",
#         {
#           "key5": "value5"
#         }
#       ],
#       "setting6": [
#         "nested",
#         {
#           "doge": [
#             "nested",
#             {
#               "wow": [
#                 "changed",
#                 [
#                   "",
#                   "so much"
#                 ]
#               ]
#             }
#           ],
#           "key": [
#             "unchanged",
#             "value"
#           ],
#           "ops": [
#             "added",
#             "vops"
#           ]
#         }
#       ]
#     }
#   ],
#   "group1": [
#     "nested",
#     {
#       "baz": [
#         "changed",
#         [
#           "bas",
#           "bars"
#         ]
#       ],
#       "foo": [
#         "unchanged",
#         "bar"
#       ],
#       "nest": [
#         "changed",
#         [
#           {
#             "key": "value"
#           },
#           "str"
#         ]
#       ]
#     }
#   ],
#   "group2": [
#     "removed",
#     {
#       "abc": 12345,
#       "deep": {
#         "id": 45
#       }
#     }
#   ],
#   "group3": [
#     "added",
#     {
#       "deep": {
#         "id": {
#           "number": 45
#         }
#       },
#       "fee": 100500
#     }
#   ]
# }
