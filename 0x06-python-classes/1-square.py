#!/usr/bin/python3
"""Creating a class Square"""


class Square:
    """Representation of a Square object"""
    def __init__(self, size: int):
        """__init__ is a default constructor for the Square class
        Args:
            size: (int) defines the size of the Square object to be created.
        """
        self.__size = size
