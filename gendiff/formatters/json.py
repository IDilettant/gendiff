"""Json-formatter module."""
import json
from typing import Dict


def format_to_json(
    diffs_tree: Dict,
) -> str:
    """Format internal representation of diffs to json-format.

    Args:
        diffs_tree: registered result of compare between two files

    Returns:
        representation of diffs in json-format
    """
    return json.dumps(diffs_tree, indent=4)
