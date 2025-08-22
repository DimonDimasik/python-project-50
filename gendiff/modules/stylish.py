def stylish(diff_str):
    """Adds indentation to the diff line"""

    lines = diff_str.split('\n')
    formatted_lines = []
    current_indent = 0
    symbols = ('+ ', '- ', '  ')

    for line in lines:
        stripped = line.strip()
        if stripped.endswith(':'):
            stripped = stripped + ' '
        if stripped.endswith('{') and not stripped.startswith(symbols):
            formatted_lines.append(' ' * current_indent + stripped)
            current_indent += 4
        elif stripped.endswith('{') and stripped.startswith(symbols):
            formatted_lines.append(' ' * (current_indent - 2) + stripped)
            current_indent += 4
        elif stripped == '}':
            current_indent -= 4
            formatted_lines.append(' ' * current_indent + stripped)
        else:
            if stripped.startswith(symbols):
                formatted_lines.append(' ' * (current_indent - 2) + stripped)
            else:
                formatted_lines.append(' ' * current_indent + stripped)

    return '\n'.join(formatted_lines)