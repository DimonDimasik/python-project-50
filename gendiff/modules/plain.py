def format_plain_value(value):
    """Converts a value to a string of the required format"""
    exceptions = ('true', 'false', 'null', '[complex value]')
    if value in exceptions:
        return value
    elif value is None:
        return 'null'
    elif isinstance(value, (int, float)):
        return f"'{str(value)}'"
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)


def separate(data):
    before, after = data.split(':')
    return before[2:], after[1:]


def display_plain(key_list, removed_dict, added_dict):
    delited = set(removed_dict.keys()) - set(added_dict.keys())
    added = set(added_dict.keys()) - set(removed_dict.keys())
    changed = set(removed_dict.keys()) & set(added_dict.keys())
    result = []
    for item in key_list:
        if item in delited:
            result.append(f"Property '{item}' was removed")
        elif item in added:
            result.append(f"Property '{item}' was added with value: {format_plain_value(added_dict[item])}")
        elif item in changed:
            result.append(f"Property '{item}' was updated. From {format_plain_value(removed_dict[item])} to {format_plain_value(added_dict[item])}")
    return '\n'.join(result)


def plain(diff_str):
    lines = diff_str.split('\n')
    path = []
    keys = []
    deleted = {}
    added = {}
    for line in lines:
        if line.startswith('  ') and line.endswith('{'):
            path.append(line[2:-3])
        elif line.startswith('- '):
            path.append(separate(line)[0])
            key = '.'.join(path)
            if line.endswith('{'):
                value = '[complex value]'
                if key not in keys:
                    keys.append(key)
                deleted.update({f'{key}': f'{value}'})
            else:
                value = separate(line)[1]
                if key not in keys:
                    keys.append(key)
                deleted.update({f'{key}': f'{value}'})
                path.pop()
        elif line.startswith('+ '):
            path.append(separate(line)[0])
            key = '.'.join(path)
            if line.endswith('{'):
                value = '[complex value]'
                if key not in keys:
                    keys.append(key)
                added.update({f'{key}': f'{value}'})
            else:
                value = separate(line)[1]
                if key not in keys:
                    keys.append(key)
                added.update({f'{key}': f'{value}'})
                path.pop()
        elif line.endswith('}'):
            if path != []:
                path.pop()
    return display_plain(keys, deleted, added)
