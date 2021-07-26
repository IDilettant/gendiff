"""Test for gendiff module."""
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.plain import plain
from gendiff.scripts.shell_parser import create_parser


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


def test_generate_diff_json_yaml_nested(
    first_file_nested_json,
    second_file_nested_yaml,
    nested_diff_result,
):
    assert generate_diff(
        first_file_nested_json,
        second_file_nested_yaml,
    ) == nested_diff_result


def test_create_parser(
    first_file_flat_json,
    second_file_flat_json,
    flat_diff_result,
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


def test_generate_diff_plain_repr(
    first_file_nested_json,
    second_file_nested_yaml,
    plain_diff_result,
):
    assert generate_diff(
        first_file_nested_json,
        second_file_nested_yaml,
        formatter=plain,
    ) == plain_diff_result
