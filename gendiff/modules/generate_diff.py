import json
import yaml


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


def format_nested_dict(data):
    """Converts a dictionary, including nested dictionaries, to a string of the required format"""
    lines = []
    for k, v in data.items():
        if not isinstance(v, dict):
            lines.append(f'{format_value(k)}: {format_value(v)}')
        else:
            lines.append(f'{format_value(k)}: {{')
            lines.append(f'{format_nested_dict(v)}')
            lines.append('}')
    return '\n'.join(lines)


def format_diff(key, value, symbol=''):
    """Creates a visual display of the diff"""
    if not isinstance(value, dict):
        return f'{symbol}{format_value(key)}: {format_value(value)}'
    else:
        result = []
        result.append(f'{symbol}{key}: {{')
        for k, v in value.items():
            result.append(format_diff(k, v))
        result.append('}')
    return '\n'.join(result) 


def key_sort(dict_1, dict_2):
    """Merges and sorts dictionary keys"""
    keys = sorted(set(dict_1.keys()) | set(dict_2.keys()))
    return keys


def build_diff(first_dict, second_dict):
    """Builds a diff for two dictionaries, including nested dictionaries"""

    def inner(first, second):
        lines = []
        key_list = key_sort(first, second)
        for item in key_list:

            if item in first and item not in second:
                if not isinstance(first[item], dict):
                    lines.append(format_diff(item, first[item], '- '))
                else:
                    lines.append(f'- {item}: {{')
                    lines.append(format_nested_dict(first[item]))
                    lines.append('}')

            if item in second and item not in first:
                if not isinstance(second[item], dict):
                    lines.append(format_diff(item, second[item], '+ '))
                else:
                    lines.append(f'+ {item}: {{')
                    lines.append(format_nested_dict(second[item]))
                    lines.append('}')

            if item in first and item in second:
                if not isinstance(first[item], dict) or not isinstance(second[item], dict):
                    if first[item] == second[item]:
                        lines.append(format_diff(item, first[item], '  '))
                    else:
                        lines.append(format_diff(item, first[item], '- '))
                        lines.append(format_diff(item, second[item], '+ '))
                else:
                    lines.append(format_diff(item, '{', '  '))
                    nested = inner(first[item], second[item])
                    if nested:
                        lines.append(nested)
                    lines.append('}')
        return '\n'.join(lines)
    result = inner(first_dict, second_dict)
    return f'{{\n{result}\n}}'


def format_string(diff_str):
    """Adds indentation to the diff line"""

    lines = diff_str.split('\n')
    formatted_lines = []
    current_indent = 0
    
    for line in lines:
        stripped = line.strip()
        if stripped.endswith(':'):
            stripped = stripped + ' '
        if not stripped:
            continue
        
        if stripped.endswith('{') and not stripped.startswith(('+ ', '- ', '  ')):
            formatted_lines.append(' ' * current_indent + stripped)
            current_indent += 4
        elif stripped.endswith('{') and stripped.startswith(('+ ', '- ', '  ')):
            formatted_lines.append(' ' * (current_indent - 2) + stripped)
            current_indent += 4
        elif stripped == '}':
            current_indent -= 4
            formatted_lines.append(' ' * current_indent + stripped)
        else:
            if stripped.startswith(('+ ', '- ', '  ')):
                formatted_lines.append(' ' * (current_indent - 2) + stripped)
            else:
                formatted_lines.append(' ' * current_indent + stripped)
    
    return '\n'.join(formatted_lines)


def open_file(file_name):
    if file_name.endswith('json'):
        return json.load(open(file_name))
    elif file_name.endswith('yaml') or file_name.endswith('yml'):
        return yaml.load(open(file_name), Loader=yaml.FullLoader)


def generate_diff(first_file, second_file):
    first_file = open_file(first_file)
    second_file = open_file(second_file)
    diff = build_diff(first_file, second_file)
    return format_string(diff)
