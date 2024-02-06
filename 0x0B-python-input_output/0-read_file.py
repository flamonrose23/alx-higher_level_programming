#!/usr/bin/python3
"""
Writing function to read file
"""


def read_file(filename=""):
    """
    Reading txt file & printing stdout
    """
    with open(filename, name="UTF8") as f:
        read_text = f.read()
        print(read_text, end="")
