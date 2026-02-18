#!/usr/bin/python3
"""Function that raises a NameError exception with a message."""


def raise_exception_msg(message=""):
    """Raise a NameError exception with a custom message.

    Args:
        message (str): The message to include in the exception.
    """
    raise NameError(message)
