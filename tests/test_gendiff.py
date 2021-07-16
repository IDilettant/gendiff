"""Test for gendiff module."""
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff(first_file, second_file, diff_result):
    assert generate_diff(first_file, second_file) == diff_result
