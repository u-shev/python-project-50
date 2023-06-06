from gendiff.formatters import stylish
from gendiff.formatters import plain
from gendiff.formatters import json


def formatting(ast, format_name='stylish'):
    formats = {
        'stylish': stylish,
        'plain': plain,
        'json': json,
    }
    if format_name in formats:
        return formats[format_name](ast)
