from backend_base.exceptions import ImproperlyConfigured


def get_value(dict, key, default=None, raise_exception=True):
    """
    Get a value from a dict.
    :param key: Key to get.
    :param default: Default value if key is not found.
    :return: Value.
    """
    if key in dict:
        return dict[key]
    if raise_exception:
        raise ImproperlyConfigured('Key not found: {}'.format(key))
