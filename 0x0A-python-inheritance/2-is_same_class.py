#!/usr/bin/python3
"""
Writing function returning specified class
"""


def is_same_class(obj, a_class):
    """
    Returning: True if object is exact instance of specified class
    Returning: False if otherwise
    """

    if type(obj) == a_class:
        return True
    return False
