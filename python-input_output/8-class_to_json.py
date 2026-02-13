#!/usr/bin/python3
"""
Module that defines a function class_to_json.
This function returns the dictionary description
of an object for JSON serialization.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of an object
    for JSON serialization.
    """
    return obj.__dict__
