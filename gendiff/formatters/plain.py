def make_string(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return value
    if value is None:
        return 'null'
    return f"'{value}'"


def rendering_node(node: dict, path='') -> str:  
    children = node.get('children')
    current_path = f"{path}{node.get('key')}"

    if node['status'] == 'root':
        lines = map(lambda child: rendering_node(child, path), children)
        result = "\n".join(filter(bool, lines))
        return result

    if node['status'] == 'nested':
        lines = map(lambda child: rendering_node(child, f"{current_path}."), children)
        result = "\n".join(filter(bool, lines))
        return result

    if node['status'] == 'changed':
        rendered_old_value = make_string(node.get('old_value'))
        rendered_new_value = make_string(node.get('new_value'))
        return f"Property '{current_path}' was updated. " \
               f"From {rendered_old_value} to {rendered_new_value}"

    if node['status'] == 'removed':
        return f"Property '{current_path}' was removed"

    if node['status'] == 'added':
        rendered_value = make_string(node.get('value'))
        return f"Property '{current_path}' was added " \
               f"with value: {rendered_value}"


def rendering(node: dict):
    return rendering_node(node)