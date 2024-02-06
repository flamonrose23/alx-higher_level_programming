#!/usr/bin/python3
"""
Writing function: JSON string to an object
"""


import json


def from_json_string(my_str):
    """
    Returning Python data struct represented by JSON string
    """
    return json.loads(my_str)
