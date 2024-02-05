#!/usr/bin/python3
"""
Writing funtion returning same class or inherited class
"""


def is_kind_of_class(obj, a_class):
    """
    Returning: True if object is instance of,
    or if object is instance of class inherited
    Returning: False if otherwise
    """

    if isinstance(obj, a_class):
        return True
    return False
