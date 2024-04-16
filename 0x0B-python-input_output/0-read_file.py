#!/usr/bin/python3
"""
This is 0-read_file module

The 0-read_file module has one function ``read_file(filename="")`` which
reads file `filename` and print out its output.
"""


def read_file(filename=""):
    """Reads file and prints its output"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
