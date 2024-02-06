#!/usr/bin/python3
"""
Writing function returning dictionary with
with simple data structure
"""


def class_to_json(obj):
    """
    Returning dict representation of object
    """
    return obj.__dict__
