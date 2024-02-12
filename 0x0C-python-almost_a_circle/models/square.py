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
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)

    def update(self, *args, **kwargs):
        """
        Updating class Square by adding public method
        *args: arguments of no-keyworded attributes
        **kwargs: arguments of key or valour attributes
        """
        if args and len(args) != 0:
            u = 0
            for ar in args:
                if u == 0:
                    if ar is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = ar
                elif u == 1:
                    self.size = ar
                elif u == 2:
                    self.x = ar
                elif u == 3:
                    self.y = ar
                u += 1

        elif kwargs and len(kwargs) != 0:
            for i, e in kwargs.items():
                if i == "id":
                    if e is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = e
                elif i == "size":
                    self.size = e
                elif i == "x":
                    self.x = e
                elif i == "y":
                    self.y = e

    def to_dictionary(self):
        """
        Returning dict represtentation of Square
        """
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
