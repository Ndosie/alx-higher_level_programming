#!/usr/bin/python3

"""Define MyList class"""


class MyList(list):
    """Inherits from list class and a new method"""

    def __init__(self):
        """initializing object"""
        super().__init__()

    def print_sorted(self):
        """sort the list and print"""
        print(sorted(self))
