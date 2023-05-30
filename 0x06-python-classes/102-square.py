#!/usr/bin/python3
"""
A Square Class
"""


class Square:
    """ represents a square """
    def __init__(self, size=0):
        """__init__
        The __init__ method initializes the size of the square.
        Attributes:
            size (:obj:`int`, optional): The size of the square.
        Raises:
            TypeError: If `size` type is not `int`.
            ValueError: If `size` is less than `0`.
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """area
        Returns the current square area.
        Attributes:
        self"""

        return self.__size ** 2

    def __lt__(self,  other):
        return self.area() < other.area()

    def __le__(self, other):
        return (self.area() <= other.area())

    def __eq__(self, other):
        return (self.area() == other.area())

    def __ne__(self, other):
        return (self.area() != other.area())

    def __get__(self, other):
        return (self.area() >= other.area())

    def __gt__(self, other):
        return (self.area() > other.area())
