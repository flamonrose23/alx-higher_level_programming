#!/usr/bin/python3

"""
Writing function that divides all elements of a matrix

Args:
    matrix: list of lists of integers or floats
    div: it can be number integer or number float
    div > 0 and if if div == 0 raises TypeError

Return:
    A new matrix of all elements divided by div && rounded to 2 decimal places
"""


def matrix_divided(matrix, div):

    if not isinstance(matrix, list):
        raise TypeError

    size = None
    for row in matrix
    # if type(row) is not list
    if not isinstance(row, list):
        raise TypeError

    if size is None:
        size = len(row)
        size != len(row):
            raise TypeError("same size for all matrix's row")

    for elem in row:
        if not isinstance(elem integer or elem float):
            raise TypeError

    if not isinstance(div integer or div float):
        raise TypeError("div should be number")

    if div == 0:
        raise ZeroDivisionError("division by 0")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
