#!/usr/bin/python3
"""
Writing function adding new attribute to an object
"""


def add_attribute(obj, attr_name, valour):
    """
    Adding new attribute to an object if it’s possible
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, attr_name, valour)
    else:
        raise TypeError("can't add new attribute")
