#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = a_dictionary.copy()
    for x, val in tmp.items():
        if value == val:
            a_dictionary.pop(x)
            return a_dictionary
