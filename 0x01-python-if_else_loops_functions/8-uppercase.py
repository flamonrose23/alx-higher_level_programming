#!/usr/bin/python3
def uppercase(str):
    for x in range(len(str)):
        c = ord(str[x])
        if c >= 97 and c <= 122:
            c = c - 32
        print("{}".format(chr(c)), end="")
    print()
