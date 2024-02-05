#!/usr/bin/python3
"""
Writing function about class inherited
"""


def inherits_from(obj, a_class):
    """
    Returning:
    True if object is instance of class inherited direct or indirect
    False if otherwise
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
