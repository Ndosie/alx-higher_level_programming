#!/usr/bin/python3
"""Defines class Rectangle that inherits from BaseGeometry"""


class Rectangle(7-base_geometry.BaseGeometry):
    """Represents Rectangle class"""

    def __init__(self, width, height):
        """Initializes the object attributes"""

        self.__width = super().integer_validator(width)
        self.__height = super().integer_validator(height)
