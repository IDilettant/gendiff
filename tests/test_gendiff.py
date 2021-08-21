"""Tests module."""
import json

from gendiff.cli import create_parser
from gendiff.scripts.gendiff import generate_diff


def test_json_flat(
    first_file_flat_json: str,
    second_file_flat_json: str,
    flat_diff_result: str,
):
    assert generate_diff(
        first_file_flat_json,
        second_file_flat_json,
    ) == flat_diff_result


def test_yaml_flat(
    first_file_flat_yml: str,
    second_file_flat_yml: str,
    flat_diff_result: str,
):
    assert generate_diff(
        first_file_flat_yml,
        second_file_flat_yml,
    ) == flat_diff_result


def test_json_nested(
    first_file_nested_json: str,
    second_file_nested_json: str,
    nested_diff_result: str,
):
    assert generate_diff(
        first_file_nested_json,
        second_file_nested_json,
    ) == nested_diff_result


def test_yaml_nested(
    first_file_nested_yaml: str,
    second_file_nested_yaml: str,
    nested_diff_result: str,
):
    assert generate_diff(
        first_file_nested_yaml,
        second_file_nested_yaml,
    ) == nested_diff_result


def test_json_yaml_nested(
    first_file_nested_json: str,
    second_file_nested_yaml: str,
    nested_diff_result: str,
):
    assert generate_diff(
        first_file_nested_json,
        second_file_nested_yaml,
    ) == nested_diff_result


def test_create_parser(
    first_file_flat_json: str,
    second_file_flat_json: str,
    flat_diff_result: str,
):
    parser = create_parser()
    args = parser.parse_args([
        str(first_file_flat_json),
        str(second_file_flat_json),
    ])
    assert generate_diff(
        args.first_file,
        args.second_file,
        formatter=args.format,
    ) == flat_diff_result


def test_plain_repr(
    first_file_nested_json: str,
    second_file_nested_yaml: str,
    plain_diff_result: str,
):
    assert generate_diff(
        first_file_nested_json,
        second_file_nested_yaml,
        formatter='plain',
    ) == plain_diff_result


def test_format_to_json(
    first_file_nested_json: str,
    second_file_nested_yaml: str,
):
    try:
        json.loads(generate_diff(
            first_file_nested_json,
            second_file_nested_yaml,
            formatter='json',
        ))
        assert True
    except json.JSONDecodeError:
        assert False
