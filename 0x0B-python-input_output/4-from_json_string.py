#!/usr/bin/python3
"""
This is 4-from_json_string module

The 4-from_json_string module has one function ``from_json_string(my_str)``
which returns Python object from JSON string `my_str`
"""
import json


def from_json_string(my_str):
    """Returns python object from json string"""

    return json.loads(my_str)
