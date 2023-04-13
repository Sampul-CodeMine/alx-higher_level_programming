#!/usr/bin/python3
"""Rectangle class Importing the BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A subclass to represent a Rectangle"""

    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """function to return the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """String representation of the rectangle object"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
