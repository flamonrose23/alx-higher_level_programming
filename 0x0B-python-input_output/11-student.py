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
        Initializing a Student by instance
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieving dict representation
        of a Student instance
        """

        nw_dict = dict()
        if type(attrs) is list and all(type(j) is str for j in attrs):
            for j in attrs:
                if j in self.__dict__:
                    nw_dict.update({j: self.__dict__[j]})
            return nw_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """
        Replacing all attributes of the Student instance
        """

        for j in json:
            self.__dict__.update({j: json[j]})
