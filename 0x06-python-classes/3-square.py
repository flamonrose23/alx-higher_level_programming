#!/usr/bin/python3

"""A module that defines a square """


class Square:
    """A class representing a square"""

    def __init__(self, size=0):
        """Initializing new square class
        Args:
            size: representing size of new square defined
        Raises:
            TypeError & ValueError
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size should be >= 0')

        self.__size = size

    def area(self):
        """
        Returns area  square of size
        """

        return (self.__size * self.__size)
