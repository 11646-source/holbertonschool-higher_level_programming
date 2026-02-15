#!/usr/bin/python3
"""
Module: task_01_pickle
Defines a CustomObject class with serialization and deserialization
using the pickle module.
"""

import pickle


class CustomObject:
    """
    A custom object with attributes:
    - name (string)
    - age (integer)
    - is_student (boolean)
    """

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes in a formatted way.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to a file.
        Returns True if successful, None if an error occurs.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
            return True
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file and return the instance.
        Returns None if an error occurs.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except Exception:
            return None
