#!/usr/bin/python3
"""Defines a square"""


class Square:
    """class square defining a square"""

    def __init__(self, size=0):
        """initializing another square
        Args: representing size of this class square
        Raises: TypeError & ValueError
        """

        if not isinstance(size, int):
            raise TypeError("if size is an integer")
        if size < 0:
            raise ValueError("if size >= 0")

        self.__size = size
