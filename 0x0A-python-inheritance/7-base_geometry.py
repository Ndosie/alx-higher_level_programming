#!/usr/bin/python3
"""Define Geometry class"""


class BaseGeometry:
    """Represents a Geometry and its attributes and methods"""

    def area(self):
        """Raises an error message"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value and raises error"""

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
