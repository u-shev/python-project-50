import os
from gendiff.parse import parse


def parser(file_path):
    if os.path.splitext(file_path) == '.yaml' or '.yml':
        format = 'yaml'
    if os.path.splitext(file_path) == '.json':
        format = 'json'
    with open(file_path) as file:
        data = file.read()
        parsed_data = parse(data, format)
        return parsed_data
