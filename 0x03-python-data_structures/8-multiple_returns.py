#!/usr/bin/python3

def multiple_returns(sentence):
    number = len(sentence)
    if number == 0:
        first_char = None
        return number, first_char
    else:
        first_char = sentence[0]
        return number, first_char
