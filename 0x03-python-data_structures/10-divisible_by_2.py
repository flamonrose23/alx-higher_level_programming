#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for number, x in enumerate(my_list):
        if x % 2 == 0:
            new_list[number] = True
        else:
            new_list[number] = False
    return(new_list)
