#!/usr/bin/python3
"""
defined module
"""


import json


def save_to_json_file(my_obj, filename):
    """
    writes an object to a text file using json
    """

    with open(filename, 'w') as myFile:
        json.dump(my_obj, myFile)
