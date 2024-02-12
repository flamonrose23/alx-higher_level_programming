#!/usr/bin/python3
"""
Creating moduls for base classic
"""


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
