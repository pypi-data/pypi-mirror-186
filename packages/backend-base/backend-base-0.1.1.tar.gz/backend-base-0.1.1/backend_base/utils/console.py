from backend_base.conf import settings


def print_debug(msg) -> None:
    """
    Prints a debug message if settings.DEBUG is True.
    :param msg: Message to print.
    :return: None
    """

    if settings.DEBUG:
        print(msg)
