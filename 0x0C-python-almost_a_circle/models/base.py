#!/usr/bin/python3

"""Define a base class"""
import json


class Base:
    """Represents a base class with its attributes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes object attributes increments __nb_objects attribute"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @static
    def to_json_string(list_dictionaries):
        """Returns JSON string representation"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)
