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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation"""

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation"""
        if json_string is None or json_string == "[]":
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns instance with all attributes set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
