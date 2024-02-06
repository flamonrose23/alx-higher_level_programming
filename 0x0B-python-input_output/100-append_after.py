#!/usr/bin/python3
"""
Writing function for seatch & update
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserting line of text to a file
    containing a specific string
    """
    nw_text = ""

    with open(filename) as f:
        for line in f:
            nw_text += line
            if search_string in line:
                nw_text += new_string

    with open(filename, "+w") as w:
        w.write(nw_text)
