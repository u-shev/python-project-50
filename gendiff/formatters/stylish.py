def make_indent(depth: int) -> str:
    return ' ' * (depth * 4 - 2)


def make_string(value, depth: int) -> str:
    if isinstance(value, bool):
        return 'true' if value else 'false'

    if value is None:
        return 'null'

    if isinstance(value, dict):
        indent = make_indent(depth)
        current_indent = indent + (' ' * 6)
        lines = []
        for k, v in value.items():
            lines.append(f'{current_indent}{k}: {make_string(v, depth + 1)}')
        result = '\n'.join(lines)
        return f'{{\n{result}\n  {indent}}}'

    return value


def rendering_node(node: dict, depth=0) -> str:  # noqa: C901
    children = node.get('children')
    indent = make_indent(depth)
    rendered_value = make_string(node.get('value'), depth)
    rendered_value_old = make_string(node.get('old_value'), depth)
    rendered_value_new = make_string(node.get('new_value'), depth)

    if node['status'] == 'root':
        lines = map(lambda child: rendering_node(child, depth + 1), children)
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'

    if node['status'] == 'nested':
        lines = map(lambda child: rendering_node(child, depth + 1), children)
        result = '\n'.join(lines)
        return f"{indent}  {node['key']}: {{\n{result}\n  {indent}}}"

    if node['status'] == 'changed':
        line1 = f"{indent}- {node['key']}: {rendered_value_old}\n"
        line2 = f"{indent}+ {node['key']}: {rendered_value_new}"
        return line1 + line2

    if node['status'] == 'unchanged':
        return f"{indent}  {node['key']}: {rendered_value}"

    if node['status'] == 'removed':
        return f"{indent}- {node['key']}: {rendered_value}"

    if node['status'] == 'added':
        return f"{indent}+ {node['key']}: {rendered_value}"


def rendering(node: dict):
    return rendering_node(node)
