#!/usr/bin/python3
"""Define Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes object attributes"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of a square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """Returns square representation as string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
