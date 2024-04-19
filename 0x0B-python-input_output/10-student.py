#!/usr/bin/python3
"""Define Student class"""


class Student:
    """Representation of student class"""

    def __init__(self, first_name, last_name, age):
        """Iniliatlizes Student object"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of student object"""

        if (isinstance(attrs, list) and
                all(isinstance(ele, str) for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
