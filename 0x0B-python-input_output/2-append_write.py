#!/usr/bin/python3
"""
Writing function appending string to a file
"""


def append_write(filename="", text=""):
    """
    Appending txt to filename
    Returning number of characters added
    """

    with open(filename, "a+", encoding="UTF8") as f:
        return f.write(text)
