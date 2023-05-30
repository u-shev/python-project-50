import os
import json
import yaml


def parser(file_path):
    if os.path.splitext(file_path) == '.json':
        return json.load(open(file_path))
    if os.path.splitext(file_path) == '.yaml' or '.yml':
        return yaml.safe_load(open(file_path))
