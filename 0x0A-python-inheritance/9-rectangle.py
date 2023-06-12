#!/usr/bin/python3
"""
defined BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """create class"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__widht = width
        self.__height = height

    def area(self):
        """create Area"""
        return self.__width * self.__height

    def __str__(self):
        """str"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
