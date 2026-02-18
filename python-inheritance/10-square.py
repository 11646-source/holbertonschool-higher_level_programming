#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square sides.
        """
        self.integer_validator("size", size)  # validate size
        self.__size = size  # private attribute
        super().__init__(size, size)  # call Rectangle with width=height=size

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
