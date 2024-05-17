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

    def update(self, *args, **kwargs):
        """Updates square object attributes"""
        if args and len(args) != 0:
            i = 0
            for arg in args:
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                elif k == 'size':
                    self.size = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def __str__(self):
        """Returns square representation as string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
