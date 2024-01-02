#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        c = ord(str[x])
        if c >= 97:
        print("{}".format(chr(c)), end="")
    print()
