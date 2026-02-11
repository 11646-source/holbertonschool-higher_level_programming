#!/usr/bin/python3
"""
Module that defines a function to convert
a JSON string into a Python object.
"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    represented by a JSON string.
    """
    import json
    return json.loads(my_str)
