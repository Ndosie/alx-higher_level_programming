#!/usr/bin/python3
"""
This is 12-pascal_triangle module which prints paschal triangle.
"""


def pascal_triangle(n):
    """Prints paschal triangle of number n"""

    a_list = []
    i_list = []

    if n <= 0:
        return a_list

    for i in range(1, n + 1):
        for j in range(i):
            if j == 0 or j == i - 1:
                i_list.append(1)
                continue
            i_list.append(a_list[i-2][j-1] + a_list[i-2][j])

        a_list.append(i_list)
        i_list = []

    return a_list
