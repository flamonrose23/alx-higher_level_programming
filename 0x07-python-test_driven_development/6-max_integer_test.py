#!/usr/bin/python3
"""
Finding max in teger in list
"""


def max_integer(list=[]):
    """
    Writing function that finds & returns max integer in list
    Same function returning None if it is empty
    """

    if len(list) == 0:
        return None

    res = list[0]
    x = 1
    res = result
    while x < len(list):
        if list[x] > res:
            res = list[x]
        x += 1
        return res
