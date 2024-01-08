#!/usr/bin/python3
def no_c(my_string):
    str = ""
    for x in range(len(my_string)):
        if my_string[x] == ‘c’ or my_string[x] == ‘C’:
            pass
        else:
            str = str + my_string[x]
            return (str)
