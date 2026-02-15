#!/usr/bin/python3
"""
Module: task_00_basic_serialization
Provides functions to serialize a Python dictionary to a JSON file
and deserialize a JSON file back into a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.
    If the file already exists, it will be replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize JSON data from a file into a Python dictionary.
    Returns the dictionary representation of the JSON data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
