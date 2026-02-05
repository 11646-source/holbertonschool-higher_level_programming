#!/usr/bin/python3
"""
This module provides a function to check if an object
is an instance of a specified class or its subclasses.
"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of a_class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class or its subclasses,
              False otherwise.
    """
    return isinstance(obj, a_class)
