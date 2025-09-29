from gendiff.formatters.stylish import is_dict

def format_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif is_dict(value):
        return '[complex value]'
    else:
        return str(f"'{value}'")


def format_deleted_lines(property):
    return f"Property '{property}' was removed"


def format_added_lines(property, value):
    return f"Property '{property}' was added with value: {value}"


def format_changed_lines(property, old_value, new_value):
    return f"Property '{property}' was updated. From {old_value} to {new_value}"


def format_diff_plain(diff):
    def inner(diff_nodes, current_path):
        lines = []
        nodes = current_path
        keys = sorted(list(diff_nodes.keys()))
        for key in keys:
            path = diff_nodes[key]['name']
            nodes.append(path)
            if diff_nodes[key]['action'] == 'deleted':
                lines.append(format_deleted_lines('.'.join(nodes)))
                if nodes != []:
                    nodes.pop()
            elif diff_nodes[key]['action'] == 'added':
                node = '.'.join(nodes)
                new_val = format_value(diff_nodes[key]['new_value'])
                lines.append(format_added_lines(node, new_val))
                if nodes != []:
                    nodes.pop()
            elif diff_nodes[key]['action'] == 'changed':
                node = '.'.join(nodes)
                old_val = format_value(diff_nodes[key]['old_value'])
                new_val = format_value(diff_nodes[key]['new_value'])
                lines.append(format_changed_lines(node, old_val, new_val))
                if nodes != []:
                    nodes.pop()
            elif diff_nodes[key]['action'] == 'unchanged':
                if nodes != []:
                    nodes.pop()
            elif diff_nodes[key]['action'] == 'nested':
                lines.extend(inner(diff_nodes[key]['children'], nodes))
                if nodes != []:
                    nodes.pop()
        return lines
    return '\n'.join(inner(diff, []))
