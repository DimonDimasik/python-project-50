import json


def assort(iter):
    return sorted(iter, key=lambda item: item[1])


def convert(iter):
    for i in iter:
        print(i[0] + i[1] + i[2])


def collate(first, second):
    compare_list = []
    for item in first:
        if item in second:
            if first[item] == second[item]:
                compare_list.append(('  ', f'{item}: '.lower(), f'{first[item]}'.lower()))
            else:
                compare_list.append(('- ', f'{item}: '.lower(), f'{first[item]}'.lower()))
                compare_list.append(('+ ', f'{item}: '.lower(), f'{second[item]}'.lower()))
        else:
            compare_list.append(('- ', f'{item}: '.lower(), f'{first[item]}'.lower()))
    for item in second:
        if item not in first:
            compare_list.append(('+ ', f'{item}: '.lower(), f'{second[item]}'.lower()))
    return compare_list


def generate_diff(first_file, second_file):
    first_file = json.load(open(first_file))
    second_file = json.load(open(second_file))
    diff_list = collate(first_file, second_file)
    diff_list = assort(diff_list)
    convert(diff_list)
