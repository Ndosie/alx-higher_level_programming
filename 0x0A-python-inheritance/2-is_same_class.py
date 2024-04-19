#!/usr/bin/python3
"""
This is 2-is_same_class module

The 2-is_same_class modul has one function `is_same_class(obj, a_class)`
which returns true if `obj` is an instance of `a_class` otherwise false.
"""


def is_same_class(obj, a_class):
    """Returns True or False if obj is an instance of a_class"""

    if type(obj) == a_class:
        return True
    else:
        return False
