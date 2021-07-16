"""Fixtures module."""
import json

import pytest


@pytest.fixture
def first_file(tmpdir):
    """First example json-file.

    Args:
        tmpdir: temporary directory fixture

    Yields:
        temporary file
    """
    json_data = {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False,
    }
    temp_file = tmpdir.join('file1.json')
    with temp_file.open(mode='w') as temp:
        json.dump(json_data, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def second_file(tmpdir):
    """Second example json-file.

    Args:
        tmpdir: temporary directory fixture

    Yields:
        temporary file
    """
    json_data = {
        'timeout': 20,
        'verbose': True,
        'host': 'hexlet.io',
    }
    temp_file = tmpdir.join('file2.json')
    with temp_file.open(mode='w') as temp:
        json.dump(json_data, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def diff_result() -> str:
    """Two json-files diff result.

    Returns:
        two json-files diff result
    """
    return """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
