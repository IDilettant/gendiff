"""Json-formatter module."""
import json
from typing import Dict

from gendiff.diff_sorter import sort_with_abc_order


def format_to_json(
    diffs_tree: Dict,
) -> str:
    """Format internal representation of diffs to json-format.

    Args:
        diffs_tree: registered result of compare between two files

    Returns:
        representation of diffs in json-format
    """
    sorted_diffs_tree = sort_with_abc_order(diffs_tree)
    return json.dumps(sorted_diffs_tree, indent=4)
