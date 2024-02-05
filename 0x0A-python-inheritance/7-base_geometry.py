#!/usr/bin/python3
"""
Writing module of class BaseGeometry
"""


class BaseGeometry:
    """
    Representing base of geometry
    """

    def area(self):
        """
        Raising Exception with message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validating integer as value
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
