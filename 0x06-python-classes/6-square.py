#!/usr/bin/python3

"""A module defining a square """


class Square:
    """A class representing a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializing new square class
        Args:
        size: representing length of size of new square defined
        position: representing position of the new square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Retrieving current position of the square
        """

        return self.__position

    @position.setter
    def position(self, value):
        """
        Setting position of the square
        Args:
            value as tuple of 2 positive integers
            Raises: TypeError if value is not a tuple or any int in tuple < 0
        """

        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([x for x in value if isinstance(x, int) and x >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """
        Returns area  square of size
        """

        return (self.__size * self.__size)

    def my_print(self):
        """
        Printing in stdout the square with the character #
        """
        if self.__size == 0:
            print()
