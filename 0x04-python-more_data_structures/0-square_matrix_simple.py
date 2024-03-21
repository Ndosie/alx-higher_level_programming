#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for m in matrix:
        squared_list = list(map(lambda x: x * x, m))
        new_list.append(squared_list)
    return new_list
