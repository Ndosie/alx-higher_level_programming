#!/usr/bin/python3

"""Define Rectangle class"""


class Rectangle:
    """Represents a rectangle with its attribute"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    def width(self):
        return self.__width

    def width(self, value):
        if type(value) != 'int':
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def height(self):
        return self.__height

    def height(self, value):
        if type(value) != 'int':
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
