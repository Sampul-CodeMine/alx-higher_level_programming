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

    def to_json(self):
        """method to get the dictionary representation of Student object"""
        return self.__dict__
