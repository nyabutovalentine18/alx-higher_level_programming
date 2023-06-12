#!/usr/bin/python3
"""
defined BaseGeometry
"""


class BaseGeometry(object):
    """
    empty class
    """

    def area(self):
        """
        defined area method
        Args: None
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        Args:
            name: string
            value: integer
        """

        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
