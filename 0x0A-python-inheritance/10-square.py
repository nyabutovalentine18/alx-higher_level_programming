#!/usr/bin/python3
"""
creates a module
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    square
    """

    def __init__(self, size):
        """
        Args:
            Size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()
