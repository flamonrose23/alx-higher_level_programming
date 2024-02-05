#!/usr/bin/python3
"""
Writing class MyList module
"""


class MyList(list):
    """
    Defining public instance method
    """

    def print_sorted(self):
        """
        Printing the list in  ascending sort
        """
        print(sorted(self))
