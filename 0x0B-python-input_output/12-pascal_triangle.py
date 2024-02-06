#!/usr/bin/python3
"""
Creating function of Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returning list of lists of integers representing
    the Pascal’s triangle of n
    """

    if n <= 0:
        return []

    triangles = [[1]]

    for x in range(1, n):
        row = [1]
        for y in range(1, x):
            row.append(triangles[x - 1][y - 1] + triangles[x - 1][y])
        row.append(1)
        triangles.append(row)

    return triangles
