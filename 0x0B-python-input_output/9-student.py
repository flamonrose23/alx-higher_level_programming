#!/usr/bin/python3
"""
Writing class Student defined by
Public instance attributes:
    first name, last name && age
"""


class Student:
    """
    Defining s student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializing a student by ()
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieving dict representation of a Student instance
        """
        return self.__dict__
