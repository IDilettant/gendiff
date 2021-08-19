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
    """
    json_ext = '.json'
    yaml_ext = ('.yaml', '.yml')
    if extension == json_ext:
        return json.loads(file_content)
    elif extension in yaml_ext:
        return yaml.safe_load(file_content)
