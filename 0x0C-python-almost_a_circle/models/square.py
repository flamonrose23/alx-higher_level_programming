#!/usr/bin/python3
"""
Creating module for Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Writing class square from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializing a Square with
        size, x, y and id
        """
        super().__init__(size, x, y, id)

    @property
    def size(self):
        """
        printing size of square
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        getting size setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returning the print and string of Rectangle
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x,  self.width, self.y)
