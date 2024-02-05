#!/usr/bin/python3
"""
Writing class Square
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Representing class Square inherited
    """
    def __init__(self, size):
        """
        Initializing a Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Returning area of Square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Returning square description and the print
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
