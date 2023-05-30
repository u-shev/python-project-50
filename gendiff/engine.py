from gendiff.parser import parser
from gendiff.ast import build_ast
from gendiff.formatter import formatting


def generate_diff(file_path1, file_path2, format_name='stylish') -> str:
    file1 = dict(parser(file_path1))
    file2 = dict(parser(file_path2))
    ast = build_ast(file1, file2)
    rendered = formatting(ast, format_name)
    return rendered
