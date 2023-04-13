#!/usr/bin/python3
"""Defining a Student Class"""


class Student:
    """Represents a Student object"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        Args:
            first_name (str): the firstname of the student
            last_name (str): the lastname of the student
            age (int): the age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """method to get the dictionary representation of Student object.
        if attr is a list of string represent only the the valid attributes in
        the string
        Args:
            attrs (list): this is an optional attribute
        Return:
            a dictionary of valid attributes if all elements are list in the
        dictionary else return the dictionary rep of the class
        """
        if type(attrs) == list:
            result = dict()
            for item in attrs:
                if type(item) == str:
                    for a in attrs:
                        if hasattr(self, a):
                            result[a] = getattr(self, a)
            return result
        return self.__dict__
