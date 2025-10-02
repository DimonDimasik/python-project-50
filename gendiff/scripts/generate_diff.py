import json
import yaml
from gendiff.formatters.format import choose_formatter
from gendiff.formatters.stylish import is_dict


def make_added(key, val):
    """Generates a dictionary with data for the added key."""
    return {'action': 'added', 'name': f'{key}', 'new_value': val}


def make_deleted(key, val):
    """Generates a dictionary with data for the deleted key."""
    return {'action': 'deleted', 'name': f'{key}', 'old_value': val}


def make_unchanged(key, val):
    """Generates a dictionary with data for the unchanged key."""
    return {'action': 'unchanged', 'name': f'{key}', 'value': val}


def make_changed(key, old_val, new_val):
    """Generates a dictionary with data for the changed key."""
    return {'action': 'changed', 'name': f'{key}',
            'old_value': old_val, 'new_value': new_val}


def make_nested(key, val):
    """Generates a dictionary with data for a key
    with a value - a dictionary."""
    return {'action': 'nested', 'name': f'{key}', 'children': val}


def find_diff(first: dict, second: dict):
    """Finds the difference between two dictionaries,
    including nested dictionaries."""
    diff = []
    keys = set(first.keys()) | set(second.keys())
    first_set = set(first.keys()) - set(second.keys())
    second_set = set(second.keys()) - set(first.keys())
    intersection = set(first.keys()) & set(second.keys())
    for item in keys:

        if item in first_set:
            diff.append(make_deleted(item, first[item]))

        elif item in second_set:
            diff.append(make_added(item, second[item]))

        elif item in intersection:
            if not is_dict(first[item]) or not is_dict(second[item]):
                if first[item] == second[item]:
                    diff.append(make_unchanged(item, first[item]))
                else:
                    diff.append(make_changed(item, first[item], second[item]))

            elif is_dict(first[item]) and is_dict(second[item]):
                nested = find_diff(first[item], second[item])
                diff.append(make_nested(item, nested))
    sorted_diff = sorted(diff, key=lambda item: item['name'])
    return sorted_diff


def open_file(file_name):
    """Opens json and yaml files."""
    if file_name.endswith('json'):
        return json.load(open(file_name))
    elif file_name.endswith('yaml') or file_name.endswith('yml'):
        return yaml.load(open(file_name), Loader=yaml.FullLoader)


def generate_diff(first_file, second_file, format_name='stylish'):
    """Creates a diff between two files."""
    first_file = open_file(first_file)
    second_file = open_file(second_file)
    diff = find_diff(first_file, second_file)
    return choose_formatter(diff, format_name)
