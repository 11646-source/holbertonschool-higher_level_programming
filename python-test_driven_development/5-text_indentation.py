#!/usr/bin/python3
"""
Module 5-text_indentation
Defines a function that prints text with 2 new lines
after '.', '?', and ':' characters.
"""

def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':'.

    Args:
        text (str): The input string to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    for char in text:
        result += char
        if char in [".", "?", ":"]:
            result += "\n\n"

    # Split into lines, strip spaces, and print
    lines = result.split("\n")
    for line in lines:
        stripped_line = line.strip()
        if stripped_line:  # Avoid printing empty lines
            print(stripped_line)


if __name__ == "__main__":
    # Example usage
    sample = "Hello. How are you? I am fine: thanks."
    text_indentation(sample)

