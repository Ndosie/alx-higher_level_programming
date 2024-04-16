#!/usr/bin/python3
"""
This is 3-to_json_string module

The 3-to_json_string module has one function ``to_json_string(my_obj)``
which returns the json representation of object `my_obj`.
"""
import json


def to_json_string(my_obj):
    """Returns the json represention of string object"""

    return json.dumps(my_obj)
