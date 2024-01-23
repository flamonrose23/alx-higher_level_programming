#!/usr/bin/python3
"""Defines a square"""


class Square:
    """class square defining a square"""

    def __init__(self, size):
        """initializing another square
        Args: representing size of this class square
        Raises: TypeError & ValueError
        """

        if type(size) is not int:
            raise TypeError("exception if size is not an integer")
        if size < 0:
            raise ValueError("exception if size >= 0")
        else:
            self.__size = size
