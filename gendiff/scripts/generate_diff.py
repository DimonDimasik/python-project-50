import json
import yaml
from gendiff.formatters.format import choose_formatter
from gendiff.formatters.stylish import is_dict


def make_added(key, val):
    return {f'{key}': {'action': 'added', 'name': f'{key}', 'new_value': val}}


def make_deleted(key, val):
    return {f'{key}': {'action': 'deleted', 'name': f'{key}', 'old_value': val}}


def make_unchanged(key, val):
    return {f'{key}': {'action': 'unchanged', 'name': f'{key}', 'value': val}}


def make_changed(key, old_val, new_val):
    return {f'{key}': {'action': 'changed', 'name': f'{key}', 'old_value': old_val, 'new_value': new_val}}


def make_nested(key, val):
    return {f'{key}': {'action': 'nested', 'name': f'{key}', 'children': val}}


def find_diff(first_dict, second_dict):
    diff = {}
    keys = set(first_dict.keys()) | set(second_dict.keys())
    first_set = set(first_dict.keys()) - set(second_dict.keys())
    second_set = set(second_dict.keys()) - set(first_dict.keys())
    intersection = set(first_dict.keys()) & set(second_dict.keys())
    for item in keys:
        if item in first_set:
            diff.update(make_deleted(item, first_dict[item]))
        elif item in second_set:
            diff.update(make_added(item, second_dict[item]))
        elif item in intersection:
            if not is_dict(first_dict[item]) or not is_dict(second_dict[item]):
                if first_dict[item] == second_dict[item]:
                    diff.update(make_unchanged(item, first_dict[item]))
                else:
                    diff.update(make_changed(item, first_dict[item], second_dict[item]))
            elif is_dict(first_dict[item]) and is_dict(second_dict[item]):
                nested = find_diff(first_dict[item], second_dict[item])
                diff.update(make_nested(item, nested))
    return diff


def open_file(file_name):
    """Opens json and yaml files"""
    if file_name.endswith('json'):
        return json.load(open(file_name))
    elif file_name.endswith('yaml') or file_name.endswith('yml'):
        return yaml.load(open(file_name), Loader=yaml.FullLoader)


def generate_diff(first_file, second_file, format_name='stylish'):
    """Creates a diff between two files"""
    first_file = open_file(first_file)
    second_file = open_file(second_file)
    diff = find_diff(first_file, second_file)
    return choose_formatter(diff, format_name)
