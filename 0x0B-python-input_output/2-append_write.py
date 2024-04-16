#!/usr/bin/python3
"""
This is 2-append_write module

The 2-append_write module has one function ``append_write(filename="", text="")``
which appends `text` to a file `filename` and returns the number of characters
written.
"""


def append_write(filename="", text=""):
    """Appends text to the end of a UTF8 text file"""

    with open(filename, mode='a', encoding='utf-8') as f:
       return f.write(text)
