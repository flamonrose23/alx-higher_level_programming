#!/usr/bin/python3
"""
Creating module for Rectangle
"""


class Rectangle(base):
    """
    Writing class Rectangle from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing class Rectangle from Base
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Printing width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        printing width of Rectangle
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Printing height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        printing height of Rectangle as valour
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x of Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        valour: x of rectangle
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y of Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        valour: y of rectangle
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
