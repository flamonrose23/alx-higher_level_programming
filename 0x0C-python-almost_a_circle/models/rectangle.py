#!/usr/bin/python3
"""
Creating module for Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    Representing class rectangle form base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializing Rectangle with
        width, height, x, y and id
        raising: typeError or ValueError
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Getting width of Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getting height of Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getting x of Rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getting y of Rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Printing area of Rectangle
        """
        return self.width * self.height

    def display(self):
        """
        Returning representation of Rectangle with character #
        """
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for r in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for s in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """
        Updating class Rectangle by adding the public method
        *args: New variables for no-keyword
        **kwargs: New valors for keyword args
        """
        if args and len(args) != 0:
            u = 0
            for arg in args:
                if u == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif u == 1:
                    self.width = arg
                elif u == 2:
                    self.height = arg
                elif u == 3:
                    self.x = arg
                elif u == 4:
                    self.y = arg
                u += 1

        elif kwargs and len(kwargs) != 0:
            for i, e in kwargs.items():
                if i == "id":
                    if e is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = e
                elif i == "width":
                    self.width = e
                elif i == "height":
                    self.height = e
                elif e == "x":
                    self.x = e
                elif i == "y":
                    self.y = e

    def to_dictionary(self):
        """
        Returning dict representated of Rectangle
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """
        Returning the print() and str() of Rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
