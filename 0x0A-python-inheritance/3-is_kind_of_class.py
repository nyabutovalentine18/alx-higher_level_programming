#!/usr/bin/python3
"""
defined is_kind_of_class function
"""


def is_kind_of_class(obj, a_class):
    """
    checks instance of a parent or child class
    Args:
        a_class
    """

    if isinstance (obj, a_class):
        return True

    else:
        return False
