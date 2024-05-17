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
        if value <= 0:
            raise ValueError('width must be > 0')
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
        if value <= 0:
            raise ValueError('height must be > 0')
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

    def area(self):
        """Returns the value of a Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Displays rectangle using # symbol"""
        for i in range(self.y):
            print("")
        for i in range(self.height):
            for i in range(self.x):
                print(" ", end="")
            print("{}".format("#" * self.width))

    def update(self, *args):
        """Updates rectange objects attributes"""
        i = 0
        for arg in args:
            if i == 0:
                self.id = arg
            elif i == 1:
                self.width = arg
            elif i == 2:
                self.height = arg
            elif i == 3:
                self.x = arg
            elif i == 4:
                self.y = arg
            i += 1

    def __str__(self):
        """Returns rectangle representation as string"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
