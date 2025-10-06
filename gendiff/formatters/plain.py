from gendiff.formatters.stylish import is_dict


def format_value(value):
    """Converts a value to a string of the required format"""
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, (int, float)):
        return str(value)
    elif value in ('True', 'true', 'False' 'false'):
        return value.lower()
    elif is_dict(value):
        return '[complex value]'
    else:
        return str(f"'{value}'")


def format_deleted_lines(property: str):
    """Generates a line with data for the deleted property."""
    return f"Property '{property}' was removed"


def format_added_lines(property: str, value):
    """Generates a line with data for the added property."""
    return f"Property '{property}' was added with value: {value}"


def format_changed_lines(property: str, old_val, new_val):
    """Generates a line with data for the changed property."""
    return f"Property '{property}' was updated. From {old_val} to {new_val}"


def format_diff_plain(diff: list):
    """Generates a diff display in 'plain' format."""
    def inner(diff_nodes, current_path):
        lines = []
        nodes = current_path
        for item in diff_nodes:
            path = item['name']
            nodes.append(path)
            if item['action'] == 'deleted':
                lines.append(format_deleted_lines('.'.join(nodes)))
                if nodes != []:
                    nodes.pop()
            elif item['action'] == 'added':
                node = '.'.join(nodes)
                new_val = format_value(item['new_value'])
                lines.append(format_added_lines(node, new_val))
                if nodes != []:
                    nodes.pop()
            elif item['action'] == 'changed':
                node = '.'.join(nodes)
                old_val = format_value(item['old_value'])
                new_val = format_value(item['new_value'])
                lines.append(format_changed_lines(node, old_val, new_val))
                if nodes != []:
                    nodes.pop()
            elif item['action'] == 'unchanged':
                if nodes != []:
                    nodes.pop()
            elif item['action'] == 'nested':
                lines.extend(inner(item['children'], nodes))
                if nodes != []:
                    nodes.pop()
        return lines
    return '\n'.join(inner(diff, []))
