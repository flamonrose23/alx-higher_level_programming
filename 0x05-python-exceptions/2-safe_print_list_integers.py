#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for m in range(x):
        try:
            print("{:d}".format(my_list[m]), end="")
        except (ValueError, TypeError):
            pass
        else:
            counter += 1
    print()
    return counter
