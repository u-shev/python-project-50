from gendiff.formatters import stylish
from gendiff.formatters import plain


def formatting(ast, format_name='stylish'):
    formats = {
            'stylish': stylish,
            'plain': plain,
            }
    if format_name in formats:
        return formats[format_name](ast)
