from typing import Union
from backend_base.exceptions import ImproperlyConfigured


def bool_from_str(value: str, raise_exception=False) -> Union[bool, None]:
    """
    Convert string to boolean.
    :param value: String to convert.
    :return: Boolean value.
    """

    if not isinstance(value, str):
        if raise_exception:
            raise ImproperlyConfigured('Value is not a string')
        return value

    if value.lower() in ['true', '1', 'yes', 'y', 't', 'True']:
        return True
    elif value.lower() in ['false', '0', 'no', 'n', 'f', 'False']:
        return False

    if raise_exception:
        raise ImproperlyConfigured(
            f'Value {value} is not a valid boolean string'
        )
    return None
