#!/usr/bin/python3
"""
This 4-print_square module

The 4-print_square module has one function called ``print_square()``
which prints `#` in a square shape according to a given size.
For example

>>> print_square(4)
####
####
####
####
"""


def print_square(size):
    """Print # in square shape according to size"""

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if size == 0:
        print()

    for i in range(size):
        print('#' * size)
