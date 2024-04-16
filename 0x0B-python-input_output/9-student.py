#!/usr/bin/python3
"""Define Student class"""


class Student:
    """Representation of student class"""

    def __init__(self, first_name, last_name, age):
        """Iniliatlizes Student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return the dictionary representation of student object"""

        return self.__dict__
