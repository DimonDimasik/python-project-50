import json
import yaml


def assort(iter):
    return sorted(iter, key=lambda item: item[1])


def convert(iter):
    string = ''
    for i in iter:
        string += i[0] + i[1] + i[2]
    return string[:-1]


def compare(first, second):
    compare_list = []
    for item in first:
        if item in second:
            if first[item] == second[item]:
                compare_list.append(
                    ('  ', f'{item}: '.lower(), f'{first[item]}\n'.lower())
                )
            else:
                compare_list.append(
                    ('- ', f'{item}: '.lower(), f'{first[item]}\n'.lower())
                )
                compare_list.append(
                    ('+ ', f'{item}: '.lower(), f'{second[item]}\n'.lower())
                )
        else:
            compare_list.append(
                ('- ', f'{item}: '.lower(), f'{first[item]}\n'.lower())
            )
    for item in second:
        if item not in first:
            compare_list.append(
                ('+ ', f'{item}: '.lower(), f'{second[item]}\n'.lower())
            )
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
    diff_list = assort(diff_list)
    return convert(diff_list)
