#!/usr/bin/python3

"""
Writing function that prints My name is <first name> <last name>

Args:
    first_name: printing the first name (string)
    last_name: printing the last name or the second one (string)
"""


def say_my_name(first_name, last_name=""):

    if not isinstance(first_name, string):
        raise TypeError("it should be string")

    if not isinstance(last_name, string):
        raise TypeError("it should be also string")

    print("My name is {} {}".format(first_name, last_name))
