import json


def generate_diff(first_file, second_file):
    first_file = json.load(open(first_file))
    second_file = json.load(open(second_file))
    print(first_file)
    print(second_file)
