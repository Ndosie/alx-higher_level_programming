#!/usr/bin/python3

"""
This is 0-lookup module.

The 0-lookup has one function `def lookup(obj)` which
returns the list of all attributes and method of `obj`.

"""


def lookup(obj):
    """Return the list of all attributes and method of obj"""

    return dir(obj)
