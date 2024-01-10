#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[s ** 2 for s in row] for row in matrix]
    return new_matrix
