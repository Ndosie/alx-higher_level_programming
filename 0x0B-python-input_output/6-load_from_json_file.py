#!/usr/bin/python3
"""
This is 6-load_from_json_file module

The 6-load_from_json_file module has one function ``load_from_jso
n_file(filename)``which load from Json file and
create and return python object.
"""
import json


def load_from_json_file(filename):
    """Load json file and create python object and return it"""

    with open(filename, encoding='utf-8') as f:
        return json.loads(f.read())
