"""Sorters for diff tree file."""
from collections import OrderedDict
from typing import Dict


def sort_with_abc_order(diffs_tree: Dict) -> OrderedDict:
    """Sort diffs tree with according alphabetical order.

    Args:
        diffs_tree: registered result of compare between two files

    Returns:
        sorted registered result of compare between two files
    """
    sorted_diffs_tree = OrderedDict()
    for key, value in sorted(diffs_tree.items()):
        sorted_diffs_tree[key] = value
        if value.get('state') == 'subtree':
            sorted_diffs_tree[key]['children_diff'] = sort_with_abc_order(value['children_diff'])
    return sorted_diffs_tree
