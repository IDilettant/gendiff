"""Find differences between two json or yaml files."""


from gendiff.file_reader import read_file
from gendiff.formatters.formats import FORMATS, STYLISH
from gendiff.inter_repr import get_diffs_tree

DEFAULT_FORMAT = STYLISH


def generate_diff(
    first_file_path: str,
    second_file_path: str,
    formatter: str = DEFAULT_FORMAT,
) -> str:
    """Find differences between two files.

    Perform result of search as string in dictionary like format

    Args:
        first_file_path: path to file
        second_file_path: path to file
        formatter: function for format to dictionary-like string

    Returns:
        Diffs in dictionary like format
    """
    first_file_data = read_file(first_file_path)
    second_file_data = read_file(second_file_path)
    diffs_tree = get_diffs_tree(first_file_data, second_file_data)
    return FORMATS[formatter](diffs_tree)  # type: ignore
