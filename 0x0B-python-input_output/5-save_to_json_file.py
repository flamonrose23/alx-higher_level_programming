#!/usr/bin/python3
"""
Writing an Object to a text file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writing representation JSON of my_obj
    """
    with open(filename, "w+") as f:
        json.dump(my_obj, f)
