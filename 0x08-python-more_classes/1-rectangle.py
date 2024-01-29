#!/usr/bin/python3
"""
Writing a class Rectangle definied on the first task
"""


class Rectangle:
    """
    Initializing new rectangle with width & height dimensions
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        retrieving property of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """definining width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieving property of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """defining height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
