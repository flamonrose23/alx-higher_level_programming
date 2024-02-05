#!/usr/bin/python3
"""
Writing class MyInt inherited
"""


class MyInt(int):
    """
    Defining MyInt as rebel integer,
    MyInt has == and != operators inverted
    """

    def __eq__(self, valour):
        """
        Overriding == operator inverted
        """
        return int(self) != int(valour)

    def __ne__(self, valour):
        """
        Overriding != operator inverted
        """
        return int(self) == int(valour)
