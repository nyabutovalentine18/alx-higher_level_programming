#!/usr/bin/python3
"""
defined module
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of text
    """

    with open(filename, 'a') as myFile:
        return (myFile.write(text))
