#!/usr/bin/python3
"""Define Square class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes object attributes"""
        super().__init__(size, size, x, y)

    def __str__(self):
        """Returns rectangle representation as string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
