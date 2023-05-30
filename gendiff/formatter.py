from gendiff.formatters import stylish


def formatting(ast, format_name='stylish'):
    formats = {
            'stylish': stylish,
            }
    if format_name in formats:
        return formats[format_name](ast)
