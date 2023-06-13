#!/usr/bin/python3
"""
defined module
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends the new_string
    """

    with open(filename, "r") as f:
        text = f.readlines()

    with open(filename, "w") as myFile:
        s = ""
        for line in text:
            s += line
            if search_string in line:
                s += new_string
        myFile.write(s)
