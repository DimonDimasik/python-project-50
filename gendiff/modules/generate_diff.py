import json
import yaml


def format_diff(key, value, symbol=''):
    if not isinstance(value, dict):
        return f'{symbol}{key}: {value}'.lower()
    else:
        result = []
        result.append(f'{key}: {{')
        for k, v in value.items():
            result.append(format_diff(k, v))
        result.append('}')
    return '\n'.join(result)
    


def key_sort(dict_1, dict_2):
    keys = sorted(set(dict_1.keys()) | set(dict_2.keys()))
    return keys


def format_string(diff_str):
    lines = diff_str.split('\n')
    formatted_lines = []
    current_indent = 0
    
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        
        if stripped.endswith('{'):
            formatted_lines.append(' ' * current_indent + stripped)
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




def build_diff(first_dict, second_dict):
    

    def inner(first, second):
        lines = []
        key_list = key_sort(first, second)
        for item in key_list:
            if item in first and item not in second:
                lines.append(format_diff(item, first[item], '- '))
            if item in second and item not in first:
                lines.append(format_diff(item, second[item], '+ '))
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
