#!/usr/bin/python3
"""Define square class"""


class Square:
    """Represents a square with its attributes"""

    def __init__(self, size):

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
