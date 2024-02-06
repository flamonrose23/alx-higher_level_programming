#!/usr/bin/python3
"""
Writing function creating object fr JSON file
"""


import json


def load_from_json_file(filename):
    """
    Creating python object from JSON filename
    """
    with open(filename) as f:
        return json.load(f)
