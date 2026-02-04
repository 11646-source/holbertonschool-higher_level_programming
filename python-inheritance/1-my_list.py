#!/usr/bin/python3
"""
This module defines a MyList class that inherits from list
and adds a method to print the list sorted in ascending order.
"""


class MyList(list):
    """Class that inherits from list and adds print_sorted method."""

    def print_sorted(self):
        """Print the list, but sorted in ascending order.

        Assumes all elements are integers.
        """
        print(sorted(self))
