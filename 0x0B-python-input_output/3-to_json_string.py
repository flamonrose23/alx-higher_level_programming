#!/usr/bin/python3
"""
Writing function returning JSON representation
"""


import json


def to_json_string(my_obj):
    """
    Defining string
    Returning JSON representation of my_obj
    """
    return json.dumps(my_obj)
