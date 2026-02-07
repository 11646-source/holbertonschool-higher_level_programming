#!/usr/bin/python3
"""
This module defines a BaseGeometry class with validation methods.
"""


class BaseGeometry:
    """BaseGeometry class with area and integer validation."""

    def area(self):
        """Raise an Exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an integer greater than 0.

        Args:
            name (str): The name of the variable (always a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
