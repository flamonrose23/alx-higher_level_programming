#!/usr/bin/python3
"""Defines a square"""


class Square:
    """class square defining a square"""

    def __init__(self, size=0):
        """initializing another square
        Args: representing size of this class square
        Raises: TypeError & ValueError
        """
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size should be >= 0")


def area(self):
    """
    Return: current area square
    """
    return (self.__size * self.__size)
