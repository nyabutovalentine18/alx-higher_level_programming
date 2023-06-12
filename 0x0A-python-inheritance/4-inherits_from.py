#!/usr/bin/python3
"""
defined inherits_from function
"""


def inherits_from(obj, a_class):
    """
    checks instance of a class that inherited from the specific class
    """

    if issubclass(type(obj), a_class) is True and type(obj) != a_class:
        return(True)
    return(False)
