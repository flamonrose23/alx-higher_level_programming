#!/usr/bin/python3
"""
Writing class Rectangle
"""


class Rectangle(BaseGeometry):
    """
    Representing Rectangle by base of geometry
    """

    def __init__(self, width, height):
        """
        Initializing a Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
