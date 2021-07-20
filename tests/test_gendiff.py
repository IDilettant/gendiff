"""Test for gendiff module."""
from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_json_flat(
    first_file_flat_json,
    second_file_flat_json,
    flat_diff_result,
):
    assert generate_diff(
        first_file_flat_json,
        second_file_flat_json,
    ) == flat_diff_result


def test_generate_diff_yaml_flat(
    first_file_flat_yml,
    second_file_flat_yml,
    flat_diff_result,
):
    assert generate_diff(
        first_file_flat_yml,
        second_file_flat_yml,
    ) == flat_diff_result


def test_generate_diff_json_nested(
    first_file_nested_json,
    second_file_nested_json,
    nested_diff_result,
):
    assert generate_diff(
        first_file_nested_json,
        second_file_nested_json,
    ) == nested_diff_result


def test_generate_diff_yaml_nested(
    first_file_nested_yaml,
    second_file_nested_yaml,
    nested_diff_result,
):
    assert generate_diff(
        first_file_nested_yaml,
        second_file_nested_yaml,
    ) == nested_diff_result
