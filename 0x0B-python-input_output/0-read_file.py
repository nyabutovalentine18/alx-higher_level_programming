#!/usr/bin/python3
"""
defined module
"""


def read_file(filename=""):
    """
    reads text file
    """

    with open(filename) as myFile:
        print(myFile.read(), end='')
