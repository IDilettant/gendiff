"""Tests module."""
import json

import pytest
from gendiff.differ import generate_diff
from gendiff.formatters.formats import JSON, PLAIN, STYLISH


@pytest.mark.parametrize(
    'first_filepath, second_filepath, diff_result, formatter',
    [
        (
            'fixtures/first_file_flat.json',
            'fixtures/second_file_flat.json',
            'fixtures/flat_diff_result.txt',
            STYLISH,
        ),
        (
            'fixtures/first_file_flat.yml',
            'fixtures/second_file_flat.yaml',
            'fixtures/flat_diff_result.txt',
            STYLISH,
        ),
        (
            'fixtures/first_file_nested.json',
            'fixtures/second_file_nested.json',
            'fixtures/nested_diff_result.txt',
            STYLISH,
        ),
        (
            'fixtures/first_file_nested.yml',
            'fixtures/second_file_nested.yml',
            'fixtures/nested_diff_result.txt',
            STYLISH,
        ),
        (
            'fixtures/first_file_nested.json',
            'fixtures/second_file_nested.yml',
            'fixtures/nested_diff_result.txt',
            STYLISH,
        ),
        (
            'fixtures/first_file_nested.json',
            'fixtures/second_file_nested.json',
            'fixtures/plain_diff_result.txt',
            PLAIN,
        ),
    ],
)
def test_gendiff(first_filepath, second_filepath, diff_result, formatter):
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
                'fixtures/first_file_nested.json',
                'fixtures/second_file_nested.yml',
                formatter=JSON,
            ),
        )
    except json.JSONDecodeError:
        raise AssertionError('File is not valid JSON file')
