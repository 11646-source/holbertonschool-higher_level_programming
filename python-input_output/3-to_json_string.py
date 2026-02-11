#!/usr/bin/python3
"""Module defines a function to that returns the JSON representation of an object to a string"""
import json

def to_json_string(my_obj):
    return json.dumps(my_obj)

