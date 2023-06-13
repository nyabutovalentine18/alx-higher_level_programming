#!/usr/bin/python3
"""
defined module
"""


import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file
    """

    with open(filename, 'r') as myFile:
        return (json.load(myFile))
