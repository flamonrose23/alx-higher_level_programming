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
        self.size = size

    @property
    def size(self):
        """
        Retrieve current size of the square
        """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size should be >= 0')
        self.__size = value

    def area(self):
        """
        Returns area  square of size
        """

        return (self.__size * self.__size)
