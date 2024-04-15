#!/usr/bin/python3
"""
This is 3-is_kind_of_class module.

The 3-is_kind_of_class module has one function ``is_kind_of_class(obj, a_class)``
which True if `obj` is an instance of `a_class` or a class that inherited from
otherwise False.
"""


def is_kind_of_class(obj, a_class):
    """Return True or False if obj is kind of a_class"""

    if isinstance(obj, a_class):
        return True
    return False
