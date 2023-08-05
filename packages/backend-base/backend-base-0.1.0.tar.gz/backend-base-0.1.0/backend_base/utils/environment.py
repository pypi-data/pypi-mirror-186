import os
from typing import Any


def get_env(name: str, default: Any = None) -> str:
    """
    Get environment variable.
    :param name: Name of the environment variable.
    :param default: Default value if environment variable is not set.
    :return: Value of environment variable.
    """
    if name in os.environ:
        return os.environ[name]
    return default
