#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolist = my_list[:]
    for number, x in enumerate(my_list):
        if x % 2 == 0:
            boolist[number] = True
        else:
            boolist[number] = False
            return(boolist)
