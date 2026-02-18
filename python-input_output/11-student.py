#!/usr/bin/python3
"""Defines a Student class."""


class Student:
    """Student class definition."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attribute names to retrieve.
                          If None, retrieve all attributes.
        Returns:
            dict: Dictionary representation of the Student.
        """
        if (isinstance(attrs, list) and
                all(isinstance(attr, str) for attr in attrs)):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance.

        Args:
            json (dict): Dictionary with attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
