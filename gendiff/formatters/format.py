from gendiff.formatters.stylish import format_diff_stylish
from gendiff.formatters.plain import format_diff_plain


def choose_formatter(diff, formatter):
    if formatter == 'stylish':
        return format_diff_stylish(diff)
    elif formatter == 'plain':
        return format_diff_plain(diff)
    else:
        raise ValueError(f'Unsupported formater: {formatter}')
