#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Represents a rectangle with its attribute"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes object attributes"""

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns width of an object"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of an object"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Returns the height of an object"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of an object"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the are of an object"""

        return self.width * self.height

    def perimeter(self):
        """Returns the perimeter of an object"""

        if self.width == 0 or self.height == 0:
            return 0

        return 2 * (self.width + self.height)

    def __str__(self):
        """Returns the string representation of an object"""

        if self.width == 0 or self.height == 0:
            return ""

        s_rep = ""
        for i in range(self.height):
            s_rep += "{}".format(str(self.print_symbol) * self.width)
            if i != self.height - 1:
                s_rep += "\n"
        return s_rep

    def __repr__(self):
        """Returns the string representation of an object"""

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Reduce the number of objects when an object is deleted"""

        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1i

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the Rectangle with the greater area"""

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')

        if rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1
