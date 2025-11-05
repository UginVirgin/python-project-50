def plain_formatter(diff):
    result = plain(diff)
    return "\n".join(result)


def plain(diff, path=""):
    lines = []

    def add_new_line(status, value, full_key):

            if status == "changed":
                lines.append(status_changed(full_key, value))
            elif status == "added":
                lines.append(status_added(full_key, value))
            elif status == "removed":
                lines.append(status_removed(full_key, value))
            elif status == "nested":
                lines.extend(plain(value, full_key))

    
    for key, (status, value) in diff.items():
        full_key = full_path(path, key)
        add_new_line(status, value, full_key)

    return lines

def full_path(path, key):
    if path == "":
        return key
    else:
        return f"{path}.{key}"


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def status_changed(key, value):
    value1, value2 = value
    value1_format = format_value(value1)
    value2_format = format_value(value2)

    return f"Property '{key}' was updated. From {value1_format} to {value2_format}"

def status_added(key, value):
    value = format_value(value)
    return f"Property '{key}' was added with value: {value}"

def status_removed(key, value):
    return f"Property '{key}' was removed"




#diff
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



# gendiff --format plain filepath1.json filepath2.json
# Property 'common.follow' was added with value: false
# Property 'common.setting2' was removed
# Property 'common.setting3' was updated. From true to null
# Property 'common.setting4' was added with value: 'blah blah'
# Property 'common.setting5' was added with value: [complex value]
# Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
# Property 'common.setting6.ops' was added with value: 'vops'
# Property 'group1.baz' was updated. From 'bas' to 'bars'
# Property 'group1.nest' was updated. From [complex value] to 'str'
# Property 'group2' was removed
# Property 'group3' was added with value: [complex value]