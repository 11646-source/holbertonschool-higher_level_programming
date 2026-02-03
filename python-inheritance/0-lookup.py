#!/usr/bin/python3
"""
This module provides a function to return the list of
available attributes and methods of an object.
"""


def lookup(obj):
    """Return the list of available attributes and methods of an object.

    Args:
        obj: Any Python object.

    Returns:
        list: A list of attribute and method names.
    """
    return dir(obj)
