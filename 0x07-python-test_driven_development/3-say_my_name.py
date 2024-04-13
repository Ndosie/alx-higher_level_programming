#!/usr/bin/python3
"""
This is "3-say_my_name" module

The 3-say_my_name module supplies one function say_my_name(). For example,

>>> say_my_name("Esther", "Ndosi")
My name is Esther Ndosi
"""


def say_my_name(first_name, last_name=""):
    """Prints the message with first_name and last_name"""

    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')

    print("My name is {} {}".format(first_name, last_name))
