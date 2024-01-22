#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    m = 0
    n_list = []
    result = 0
    for m in range(0, list_length):
        try:
            result = (my_list_1[m] / my_list_2[m])
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by zero")
        except IndexError:
            result = 0
            print("out of range")
        finally:
            n_list.append(result)
    return n_list
