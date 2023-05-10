from gendiff.parser import parser


def generate_diff(file_path1, file_path2):
    file1, file2 = parser(file_path1, file_path2)
    sorted_keys = sorted({**file1, **file2})
    result = '{\n'
    for key in sorted_keys:
        if key in file1 and key in file2 and file1[key] == file2[key]:
            result += f'   {key}: {file1[key]}\n'
        if key in file1 and key in file2 and file1[key] != file2[key]:
            result += f' - {key}: {file1[key]}\n + {key}: {file2[key]}\n'
        if key in file1 and key not in file2:
            result += f' - {key}: {file1[key]}\n'
        if key not in file1 and key in file2:
            result += f' + {key}: {file2[key]}\n'
    result += '}'
    result = result.lower()
    return result
