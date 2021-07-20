"""Test for gendiff module."""
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_json(first_file_json, second_file_json, flat_diff_result):
    assert generate_diff(first_file_json, second_file_json) == flat_diff_result


def test_generate_diff_yaml(first_file_yml, second_file_yml, flat_diff_result):
    assert generate_diff(first_file_yml, second_file_yml) == flat_diff_result
