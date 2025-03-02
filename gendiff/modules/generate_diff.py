import json
import yaml


def key_sort(iter):
    return sorted(iter, key=lambda item: item[1])


def convert(iter):
    string = ''
    for i in iter:
        string += i[0] + i[1] + i[2]
    return string[:-1]


def show_diff(symbol, key, value):
    return (symbol, f'{key}: '.lower(), f'{value}\n'.lower())


def compare(first, second):
    compare_list = []
    for item in first:
        if item in second:
            if first[item] == second[item]:
                compare_list.append(show_diff('  ', item, first[item]))
            else:
                compare_list.append(show_diff('- ', item, first[item]))
                compare_list.append(show_diff('+ ', item, second[item]))
        else:
            compare_list.append(show_diff('- ', item, first[item]))
    for item in second:
        if item not in first:
            compare_list.append(show_diff('+ ', item, second[item]))
    return compare_list


def open_file(file_name):
    if file_name.endswith('json'):
        return json.load(open(file_name))
    elif file_name.endswith('yaml') or file_name.endswith('yml'):
        return yaml.load(open(file_name), Loader=yaml.FullLoader)


def generate_diff(first_file, second_file):
    first_file = open_file(first_file)
    second_file = open_file(second_file)
    diff_list = compare(first_file, second_file)
    diff_list = key_sort(diff_list)
    return convert(diff_list)
