#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents Rectangle class"""

    def __init__(self, width, height):
        """Initializes the object attributes"""

        self.__width = super().integer_validator(width)
        self.__height = super().integer_validator(height)
