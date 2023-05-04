import json


def generate_diff(file_path1, file_path2):
    diff_list = ''
    first_file = dict(json.load(open(file_path1)))
    second_file = dict(json.load(open(file_path2)))

    cross_files_keys = first_file.keys() & second_file.keys()
    file1_unique_keys = first_file.keys() - second_file.keys()
    file2_unique_keys = second_file.keys() - first_file.keys()

    for key in cross_files_keys:
        if first_file[key] == second_file[key]:
            diff_list += f"  {key}: {first_file[key]}\n"
        else:
            diff_list += f"- {key}: {first_file[key]}\n"
            diff_list += f"+ {key}: {second_file[key]}\n"
    for key in file1_unique_keys:
        diff_list += f"- {key}: {first_file[key]}\n"
    for key in file2_unique_keys:
        diff_list += f"+ {key}: {second_file[key]}\n"

    return "{\n" + diff_list.lower() + "}"
