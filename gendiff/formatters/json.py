import json


def format_diff_json(diff):
    """Generates a diff display in 'json' format."""
    return json.dumps(diff, indent=4)
