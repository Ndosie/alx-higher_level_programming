#!/usr/bin/python3
"""
This is 4-inherits_from module

The 4-inherits_from module has one function ``inherits_from(obj, a_class)``
which return True if `obj` inherit from `a_class` otherwise False
"""


def inherits_from(obj, a_class):
    """Returns True or False if obj inherits from a_class"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
