#!/usr/bin/python3
def max_integer(my_list=[]):
    number = len(my_list)
    if number == 0:
        return None
    z = my_list[0]
    for x in my_list:
        if x > z:
            z = x
    return z
