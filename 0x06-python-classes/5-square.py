#!/usr/bin/python3
"""Define square class"""


class Square:
    """Represents a square with its attributes"""

    def __init__(self, size=0):
        """Initializes a square object"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square with the # character."""
        if self.size == 0:
            print ""

        for i in range(self.size):
            print("{}".format("#" * self.size))
