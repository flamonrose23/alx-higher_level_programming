#!/usr/bin/python3
"""
Writing class Student defined by
Public instance attributes:
    first name, last name && age
"""


class Student:
    """
    Representing a student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializing a student by ()
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieving dict representation of a Student instance
        """
        my_dict = {}
        if attrs is None:
            return self.__dict__
        for x in attrs:
            if hasattr(self, x):
                my_dict[x] = getattr(self, x)
                return (my_dict)
