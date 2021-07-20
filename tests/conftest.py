"""Fixtures module."""
import json
from typing import Dict

import pytest
import yaml


@pytest.fixture
def first_file_content_flat() -> Dict:
    """File content with flat structure.

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
def second_file_content_flat() -> Dict:
    """File content with flat structure.

    Returns:
        file content
    """
    return {
        'timeout': 20,
        'verbose': True,
        'host': 'hexlet.io',
    }


@pytest.fixture
def first_file_flat_json(tmpdir, first_file_content_flat: Dict):  # noqa: WPS442
    """First example json-file with flat structure.

    Args:
        tmpdir: temporary directory fixture
        first_file_content_flat: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file1.json')
    with temp_file.open(mode='w') as temp:  # noqa WPS204
        json.dump(first_file_content_flat, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def second_file_flat_json(tmpdir, second_file_content_flat: Dict):  # noqa: WPS442 E501
    """Second example json-file with flat structure.

    Args:
        tmpdir: temporary directory fixture
        second_file_content_flat: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file2.json')
    with temp_file.open(mode='w') as temp:
        json.dump(second_file_content_flat, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def first_file_flat_yml(tmpdir, first_file_content_flat: Dict):  # noqa: WPS442
    """First example yaml-file with flat structure.

    Args:
        tmpdir: temporary directory fixture
        first_file_content_flat: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file1.yaml')
    with temp_file.open(mode='w') as temp:
        yaml.dump(first_file_content_flat, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def second_file_flat_yml(tmpdir, second_file_content_flat: Dict):  # noqa: WPS442 E501
    """Second example yaml-file with flat structure.

    Args:
        tmpdir: temporary directory fixture
        second_file_content_flat: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file2.yml')  # check with alternate extension name
    with temp_file.open(mode='w') as temp:
        yaml.dump(second_file_content_flat, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def flat_diff_result() -> str:
    """Two json-files with flat structure diff result.

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
}
"""  # noqa: WPS462


@pytest.fixture
def first_file_content_nested() -> Dict:
    """File content with nested structure.

    Returns:
        file content
    """
    return {
        'common': {
            'setting1': 'Value 1',
            'setting2': 200,
            'setting3': True,
            'setting6': {
                'key': 'value',
                'doge': {
                    'wow': '',
                },
            },
        },
        'group1': {
            'baz': 'bas',
            'foo': 'bar',
            'nest': {
                'key': 'value',
            },
        },
        'group2': {
            'abc': 12345,
            'deep': {
                'id': 45,
            },
        },
    }


@pytest.fixture
def second_file_content_nested() -> Dict:
    """File content with nested structure.

    Returns:
        file content
    """
    return {
        'common': {
            'follow': False,
            'setting1': 'Value 1',
            'setting3': None,
            'setting4': 'blah blah',
            'setting5': {
                'key5': 'value5',
            },
            'setting6': {
                'key': 'value',
                'ops': 'vops',
                'doge': {
                    'wow': 'so much',
                },
            },
        },
        'group1': {
            'foo': 'bar',
            'baz': 'bars',
            'nest': 'str',
        },
        'group3': {
            'deep': {
                'id': {
                    'number': 45,
                },
            },
            'fee': 100500,
        },
    }


@pytest.fixture
def first_file_nested_yaml(tmpdir, first_file_content_nested: Dict):  # noqa: WPS442 E501
    """First example yaml-file with flat structure.

    Args:
        tmpdir: temporary directory fixture
        first_file_content_nested: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file1.yaml')
    with temp_file.open(mode='w') as temp:
        yaml.dump(first_file_content_flat, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def second_file_nested_yaml(tmpdir, second_file_content_nested: Dict):  # noqa: WPS442 E501
    """First example yaml-file with flat structure.

    Args:
        tmpdir: temporary directory fixture
        second_file_content_nested: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file2.yaml')
    with temp_file.open(mode='w') as temp:
        yaml.dump(first_file_content_flat, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def first_file_nested_json(tmpdir, first_file_content_nested: Dict):  # noqa: WPS442 E501
    """First example yaml-file with flat structure.

    Args:
        tmpdir: temporary directory fixture
        first_file_content_nested: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file1.yaml')
    with temp_file.open(mode='w') as temp:
        json.dump(first_file_content_flat, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def second_file_nested_json(tmpdir, second_file_content_nested: Dict):  # noqa: WPS442 E501
    """First example yaml-file with flat structure.

    Args:
        tmpdir: temporary directory fixture
        second_file_content_nested: file content

    Yields:
        temporary file
    """
    temp_file = tmpdir.join('file2.yaml')
    with temp_file.open(mode='w') as temp:
        json.dump(first_file_content_flat, temp)
    yield temp_file
    temp_file.remove()


@pytest.fixture
def nested_diff_result() -> str:
    """Two json-files with flat structure diff result.

    Returns:
        two json-files diff result
    """
    return """{
    common: {
      + follow: False
        setting1: Value 1
      - setting2: 200
      - setting3: True
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
"""  # noqa: WPS462 W291
