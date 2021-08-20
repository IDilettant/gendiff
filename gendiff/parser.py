"""Parser module."""
import json
from typing import Dict

import yaml


def parse_file_content(  # type: ignore
    file_content: str,
    extension: str,
) -> Dict:
    """Parse content from JSON or YAML file.

    Args:
        file_content: content from file
        extension: extension of file

    Returns:
        converted content

    Raises:
        ValueError: if extension is unexpected
    """
    json_ext = '.json'
    yaml_ext = ('.yaml', '.yml')
    extension = extension.lower()
    if extension == json_ext:
        return json.loads(file_content)
    elif extension in yaml_ext:
        return yaml.safe_load(file_content)
    raise ValueError(
        'Unexpected file extension: {0}. Expect JSON or YAML'.format(extension),
    )
