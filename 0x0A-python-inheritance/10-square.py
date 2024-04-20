#!/usr/bin/python3
"""Defines class Square which inherits from Rectangle Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents Square class"""

    def __init__(self, size):
        """Initializes object attributes"""

        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """Returns the area of square"""

        return self.__size * self.__size
