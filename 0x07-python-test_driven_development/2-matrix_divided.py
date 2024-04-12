#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Returns the new martix divided by the number div"""

    return all([[type(i) in [int, float] for i in r] for r in matrix])

matrix = [
    [1, 2, 'a'],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
