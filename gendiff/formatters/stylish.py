def format_value(value):
    """Converts a value to a string of the required format"""
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, str):
        return value
    return str(value)


def is_dict(value):
    """Checks if a value is a dictionary"""
    return True if isinstance(value, dict) else False


def format_dict(key, val):
    if not is_dict(val):
        return f'{key}: {format_value(val)}'
    else:
        lines = []
        lines.append(f'{key}: {{')
        for k, v in val.items():
            lines.append(format_dict(k, v))
        lines.append('}')
        return '\n'.join(lines)


def format_lines(diff):
    def inner(diff):
        lines = []
        keys = sorted(list(diff.keys()))
        for key in keys:
            if diff[key]['action'] == 'deleted':
                lines.append('- ' + format_dict(diff[key]['name'], diff[key]['old_value']))
            elif diff[key]['action'] == 'added':
                lines.append('+ ' + format_dict(diff[key]['name'], diff[key]['new_value']))
            elif diff[key]['action'] == 'changed':
                lines.append('- ' + format_dict(diff[key]['name'], diff[key]['old_value']))
                lines.append('+ ' + format_dict(diff[key]['name'], diff[key]['new_value']))
            elif diff[key]['action'] == 'unchanged':
                lines.append('  ' + format_dict(diff[key]['name'], diff[key]['value']))
            elif diff[key]['action'] == 'nested':
                lines.append('  ' + f"{diff[key]['name']}: {{")
                nested = inner(diff[key]['children'])
                lines.append(nested)
                lines.append('}')
        return '\n'.join(lines)
    return f'{{\n{inner(diff)}\n}}'


def make_indent(diff_str):
    """Adds indentation to the diff line"""
    lines = diff_str.split('\n')
    formatted_lines = []
    current_indent = 0
    symbols = ('+ ', '- ', '  ')   
    for line in lines:
        stripped = line.strip()
        if stripped.endswith(':'):
            stripped = stripped + ' '
        if stripped.endswith('{') and not stripped.startswith(symbols):
            formatted_lines.append(' ' * current_indent + stripped)
            current_indent += 4
        elif stripped.endswith('{') and stripped.startswith(symbols):
            formatted_lines.append(' ' * (current_indent - 2) + stripped)
            current_indent += 4
        elif stripped == '}':
            current_indent -= 4
            formatted_lines.append(' ' * current_indent + stripped)
        else:
            if stripped.startswith(symbols):
                formatted_lines.append(' ' * (current_indent - 2) + stripped)
            else:
                formatted_lines.append(' ' * current_indent + stripped)
    return '\n'.join(formatted_lines)


def format_diff_stylish(diff):
    diff_lines = format_lines(diff)
    return make_indent(diff_lines)