#!/usr/bin/python3
"""Defining class Square"""


class Square:
    """representing another new square"""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


def area(self):
    """
    Return: current area square
    """
    return (self.__size * self.__size)
