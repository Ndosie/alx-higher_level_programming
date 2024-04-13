#!/usr/bin/python3
"""
This is the "2-matrix_divided" module

The 2-matrix_divided module supplies one function, matrix_divided().
For example,

>>> matrix_divided([[2, 4, 6], [8, 10, 12]], 2)
[[1.0, 2.0, 3.0],[4.0, 5.0, 6.0]]
"""


def matrix_divided(matrix, div):
    """Returns the new martix divided by the number div"""
    new_matrix = []
    new_list = []

    if matrix is None or not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError('matrix must be a matrix '
                        '(list of lists) of integers/floats')

    length = len(matrix[0])

    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    for i in range(len(matrix)):
        if len(matrix[i]) != length:
            raise TypeError('Each row of the matrix must have the same size')
        for j in range(len(matrix[i])):
            if type(matrix[i][j]) not in [int, float]:
                raise TypeError('matrix must be a matrix '
                                '(list of lists) of integers/floats')
            else:
                new_list.append(round(matrix[i][j] / div, 2))
        new_matrix.append(new_list)
        new_list = []

    return new_matrix
