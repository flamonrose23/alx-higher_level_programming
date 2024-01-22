#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    number = 0
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end="")
            number = number + 1
        except (TypeError, ValueError):
            pass
        print("")
        return number
