#!/usr/bin/python3
"""
defined module
"""



import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


try:
    myList = load_from_json_file("add_item.json")
except FileNotFoundError:
    myList = []

for arg in range(1, len(sys.argv)):
    myList.append(sys.argv[arg])

save_to_json_file(myList, "add_item.json")
