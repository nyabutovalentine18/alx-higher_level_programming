#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """The class defines a square and checks the size attribute"""

    def __inti__(self, __size=0):
        """__init__
        the __init__  function instantiate only positive integers
        Attributes:        
        Size(:obj:`int`, optional): The size of the square
        Raises:
        TypeError and ValueError"""

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
