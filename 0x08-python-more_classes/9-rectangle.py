#!/usr/bin/python3
"""
defining a class Rectangle
"""


class Rectangle:
    """
    Initialzing rectangle class with width and height
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """
        Printing  value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Printing  value of width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returning value of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Returning value of height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Printing  the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Printing  the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """
        Modifying the special method
        """
        string = ""
        if self.__height == 0 or self.__width == 0:
            return string
        for x in range(self.__height):
            for y in range(self.__width):
                string += '#'
            if x < self.__height - 1:
                string += '\n'
        return string

    def __repr__(self):
        """
        Modifying special method of representation
        """
        return "Rectangle(" + str(self.__width) + ', ' + str(self.__height)+')'

    def __del__(self):
        """
        Printing message when instance of Rectangle is deleted
        """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returning the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returning new Rectangle instance with width == height == size
        """
        return cls(width, height)
