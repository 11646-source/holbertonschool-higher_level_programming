#!/usr/bin/python3
"""
Module that defines a function to append a UTF-8 text file and print its content.
"""


def append_write(filename="", text=""):
    """writes a string that append to a UTF-8 text and returns the number of characters written."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
