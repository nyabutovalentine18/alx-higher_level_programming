#!/usr/bin/python3
"""
defined is_same_class function
"""


def is_same_class(obj, a_class):
    """
    is_same_class checks the instance of a class
    Args:
        obj
        a_class
    """

    if type(obj) == a_class:
        return True

    else:
        return False 
