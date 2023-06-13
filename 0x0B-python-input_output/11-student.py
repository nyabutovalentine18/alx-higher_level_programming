#!/usr/bin/python3
"""
defined module
"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """Initializes an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary"""

        dic = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                dic[i] = getattr(self, i)
        return dic

    def reload_from_json(self, json):
        """replaces all attributes of the student instance"""

        for k, v in json.items():
            if hasattr(self, k):
                setattr(self, k, v)
