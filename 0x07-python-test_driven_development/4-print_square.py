#!/usr/bin/python3

"""
Writing function that prints square with character #

Args:
    size: length of square
"""


def print_square(size):

    if type(size) is not int:
        raise TypeError("it should be integer")

    if size < 0:
        raise ValueError("it should be >= 0")

    for x in range(size):
        print("#" * size)
