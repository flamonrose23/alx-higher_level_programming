#!/usr/bin/python3
"""
Creating module for base classic
"""
import json
import csv
import turtle


class Base:
    """
    Representation class for base test
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        class constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returning JSON string representation of list_dict
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returning string representation of list_dictionaries
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)
