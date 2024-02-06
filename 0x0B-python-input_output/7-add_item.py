#!/usr/bin/python3
"""
Writing script adding all arguments
"""


import json
import os.path
import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


nw_list = []


name_file = "add_item.json"


if os.path.exists(name_file) and os.path.getsize(name_file) > 0:
    nw_list = load_from_json_file(name_file)

if len(sys.argv) > 1:
    for element in sys.argv[1:]:
        nw_list.append(element)
