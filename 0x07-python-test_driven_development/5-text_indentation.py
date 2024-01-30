#!/usr/bin/python2
"""
Writing funct printing txt with 2 new lines after each of some characters
"""


def text_indentation(text):
    """
    Printing txt with 2 newlines after:
    '.', '?' and ':'
    """

    if not isinstance(text, string):
        raise TypeError("text must be a string")

    delimeter = 0
    for x in text:
        if delimeter == 0:
            if x == ' ':
                continue
            else:
                delimeter = 1
        if delimeter == 1:
            if x == '?' or x == '.' or x == ':':
                print(x)
                print()
                delimeter = 0
            else:
                print(x, end="")
