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
    value1_form = format_value(value1)
    value2_form = format_value(value2)

    return f"Property '{key}' was updated. From {value1_form} to {value2_form}"


def status_added(key, value):
    value = format_value(value)
    return f"Property '{key}' was added with value: {value}"


def status_removed(key, value):
    return f"Property '{key}' was removed"
