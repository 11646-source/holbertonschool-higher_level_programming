#!/usr/bin/python3
"""
Module class that defines a student public attribute.
"""


def _init(self, first_name, last_name, age ):
    """
    Initilize a new student public attribute.
    """
    self.first_name = first_name
    self.last_name = last_name
    self.age = age

    def to_json(self):
        """
        Retrieve a dictionary representation of the Student instance.
        """

        return self.__dict__
    
