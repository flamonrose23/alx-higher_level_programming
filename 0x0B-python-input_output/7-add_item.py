#!/usr/bin/python3
"""
Writing script adding all arguments
"""


import json
import os.path
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


my_list = []
if path.isfile("add_item.json"):
    my_list = load_from_json_file("add_item.json")

save_to_json_file(my_list + sys.argv[1:], "add_item.json")
