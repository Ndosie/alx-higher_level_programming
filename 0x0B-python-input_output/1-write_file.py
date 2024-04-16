#!/usr/bin/python3
"""
This is 1-write_file module

The 1-write_file module has one function ``write_file(filename="", text="")``
which writes `text` to a file `filename` and return the written characters.
"""


def write_file(filename="", text=""):
    """Writes text to a file"""

    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
