from gendiff.formatters import stylish
from gendiff.formatters import plain
from gendiff.formatters import json


def formatting(ast, format_name='stylish'):
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json,
    }
    return formats[format_name](ast)
