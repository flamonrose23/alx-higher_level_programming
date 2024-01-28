#!/usr/bin/python3

"""
Writing function that adds 2 integers
"""

def add_integer(a, b=98):
    """
    Arguments:
    a & b are integers // b is integer with value of 98

    Returns:
    addition of a & b
    """

    if type(a) is not (int, float):
        raise TypeError("a should be an integer")
    if type(b) is not (int, float):
        raise TypeError("b shoud be an integer")

    if type(a) is float:
        a = int(a)

    if type(b) is float:
        b = int(b)

    return (int(a) + int(b))
