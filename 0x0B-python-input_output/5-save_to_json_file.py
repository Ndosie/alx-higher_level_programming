#!/usr/bin/python3
"""
This is 5-save_to_json_file module

The 5-save_to_json_file module has one function ``save_to_json_file
(my_obj, filename)`` which writes an object to a file using Json
string representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to file using JSON string"""

    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
