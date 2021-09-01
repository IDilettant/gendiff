"""Tests module."""
import json

import pytest
from gendiff.differ import generate_diff
from gendiff.formatters.formats import JSON, PLAIN, STYLISH


@pytest.mark.parametrize(
    'first_filepath, second_filepath, diff_result, formatter',
    [
        (
            'tests/fixtures/first_file_flat.json',
            'tests/fixtures/second_file_flat.json',
            'tests/fixtures/flat_diff_result',
            STYLISH,
        ),
        (
            'tests/fixtures/first_file_flat.yml',
            'tests/fixtures/second_file_flat.yaml',
            'tests/fixtures/flat_diff_result',
            STYLISH,
        ),
        (
            'tests/fixtures/first_file_nested.json',
            'tests/fixtures/second_file_nested.json',
            'tests/fixtures/nested_diff_result',
            STYLISH,
        ),
        (
            'tests/fixtures/first_file_nested.yml',
            'tests/fixtures/second_file_nested.yml',
            'tests/fixtures/nested_diff_result',
            STYLISH,
        ),
        (
            'tests/fixtures/first_file_nested.json',
            'tests/fixtures/second_file_nested.yml',
            'tests/fixtures/nested_diff_result',
            STYLISH,
        ),
        (
            'tests/fixtures/first_file_nested.json',
            'tests/fixtures/second_file_nested.json',
            'tests/fixtures/plain_diff_result',
            PLAIN,
        ),
        (
            'tests/fixtures/hexlet_check_file1.json',
            'tests/fixtures/hexlet_check_file2.json',
            'tests/fixtures/hexlet_check_result_plain',
            PLAIN,
        ),
    ],
)
def test_gendiff(first_filepath: str, second_filepath: str, diff_result: str, formatter: str):
    with open(diff_result) as diff:
        assert generate_diff(
            first_filepath,
            second_filepath,
            formatter,
        ) == diff.read()


def test_format_to_json():
    try:
        assert json.loads(
            generate_diff(
                'tests/fixtures/first_file_nested.json',
                'tests/fixtures/second_file_nested.yml',
                formatter=JSON,
            ),
        )
    except json.JSONDecodeError:
        raise AssertionError('File is not valid JSON file')
