#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str5 = " and is greater than 5"
str0 = " and is 0"
str6 = " and is less than 6 and not 0"
if number < 0:
    lastdigit = number % -10
else:
    lastdigit = number % 10
if lastdigit > 5:
    print("Last digit of {} is {}".format(number, last) + str5)
elif lastdigit == 0:
    print("Last digit of {} is {}".format(number, last) + str0)
else:
    print("Last digit of {} is {}".format(number, last) + str6)
