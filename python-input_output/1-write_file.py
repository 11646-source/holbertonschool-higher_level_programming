#!/usr/bin/python3
"""Module that defines a function to write a UTF-8 text file and print its content."""
def write_file(filename="", text=""):
    """writes a string to a UTF-8 text and returns the number of characters written."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
