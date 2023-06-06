def make_ast(file1, file2):
    keys = file1.keys() | file2.keys()
    result = []
    for key in sorted(keys):
        child1 = file1.get(key)
        child2 = file2.get(key)

        if key not in file1:
            result.append({
                'key': key,
                'status': 'added',
                'value': child2,
            })
        elif key not in file2:
            result.append({
                'key': key,
                'status': 'removed',
                'value': child1,
            })
        elif isinstance(child1, dict) and isinstance(child2, dict):
            result.append({
                'key': key,
                'status': 'nested',
                'children': make_ast(child1, child2),
            })
        elif child1 == child2:
            result.append({
                'key': key,
                'status': 'unchanged',
                'value': child1,
            })
        else:
            result.append({
                'key': key,
                'status': 'changed',
                'old_value': child1,
                'new_value': child2,
            })
    return result


def build_ast(file1: dict, file2: dict):
    return {
        'status': 'root',
        'children': make_ast(file1, file2)
    }
