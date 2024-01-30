#!/usr/bin/python3
"""Defining a class LockedClass"""


class LockedClass:
    """
    Preventing the user from dynamically creating new instance attributes
    """

    __slots__ = ["first_name"]
