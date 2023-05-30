#!/usr/bin/python3
"""This module defines a Square class
The size attribute is only positive numbers"""


class Square:
    """The class defines a square and checks the size attribute"""

    def __inti__(self, size=0):
        """ this function instantiate only positive integers"""

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
