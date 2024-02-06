#!/usr/bin/python3
"""
Writing string to txt file
"""


def write_file(filename="", text=""):
    """
    Writing txt in filename
    Returning number of characters written
    """

    with open(filename, "w+", encoding="UTF8") as f:
        return f.write(text)
