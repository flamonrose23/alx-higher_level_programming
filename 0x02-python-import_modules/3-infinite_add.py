#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    def add_arg(argv):
        n = len(argv) - 1
        if n == 0:
            print("{:d}".format(n))
            return
        else:
        x = 1
        add = 0
        while x <= n:
            add += int(argv[x])
            x += 1
        print("{:d}".format(add))
