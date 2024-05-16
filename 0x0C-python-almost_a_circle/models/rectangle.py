#!/usr/bin/python3

"""Defines a rectangle class that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """Represents rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes object attributes"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width of a rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get height of a rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def x(self):
        """Get x coordinate of a rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x coordinate of a rectangle"""
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Get y coordinate of a rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y coordinate of a rectangle"""
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value
