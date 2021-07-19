"""Fixtures module."""
import json
from typing import Dict

import pytest
import yaml


@pytest.fixture
def first_file_content() -> Dict:
    """File content.

    Returns:
        file content
    """
    return {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False,
    }


@pytest.fixture
def second_file_content() -> Dict:
    """File content.

    Returns:
        file content
    """
    return {
        'timeout': 20,
        'verbose': True,
        'host': 'hexlet.io',
    }


@pytest.fixture
def first_file_json(tmpdir, first_file_content: Dict):  # noqa: WPS442
    """First example json-file.

    Args:
        tmpdir: temporary directory fixture
        first_file_content: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file1.json')
    with temp_file.open(mode='w') as temp:
        json.dump(first_file_content, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def second_file_json(tmpdir, second_file_content: Dict):  # noqa: WPS442
    """Second example json-file.

    Args:
        tmpdir: temporary directory fixture
        second_file_content: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file2.json')
    with temp_file.open(mode='w') as temp:
        json.dump(second_file_content, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def first_file_yml(tmpdir, first_file_content: Dict):  # noqa: WPS442
    """First example yaml-file.

    Args:
        tmpdir: temporary directory fixture
        first_file_content: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file1.yaml')
    with temp_file.open(mode='w') as temp:
        yaml.dump(first_file_content, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def second_file_yml(tmpdir, second_file_content: Dict):  # noqa: WPS442
    """Second example yaml-file.

    Args:
        tmpdir: temporary directory fixture
        second_file_content: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file2.yml')  # check with alternate extension name
    with temp_file.open(mode='w') as temp:
        yaml.dump(second_file_content, temp)
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
