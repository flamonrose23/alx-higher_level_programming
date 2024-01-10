#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search == r else r for r in my_list]
