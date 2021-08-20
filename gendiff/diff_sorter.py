"""Sorters for diff tree file."""
from collections import OrderedDict


def sort_with_abc_order(diffs_tree):
    sorted_diffs_tree = OrderedDict()
    for key, value in sorted(diffs_tree.items()):
        sorted_diffs_tree[key] = value
        if value.get('state') == 'subtree':
            sorted_diffs_tree[key]['children_diff'] = sort_with_abc_order(value['children_diff'])
    return sorted_diffs_tree
