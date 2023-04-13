#!/usr/bin/python3
"""Class that imports Rectangle as a Baseclass knowing that
Rectangle is a ChildClass to BaseGeometry class"""


BaseGeometry = __import__('6-base_geometry').BaseGeometry

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Class representing a Square Object"""

    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """"returns the area of the square"""
        return self.__size ** 2

    def __str__(self):
        """informal string reepresentation of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
