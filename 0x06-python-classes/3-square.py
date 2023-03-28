#!/usr/bin/python3
"""Creating a class Square"""


class Square:
    """Representation of a Square object"""

    def __init__(self, size=0):
        """__init__ is a default constructor for the Square class
        Args:
            size: (int) defines the size of the Square object to be created.
        """
        if isinstance(size, int):
            if size >= 0:
                self.__size = size
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """Function to calculate the area of a circle
        Returns:
            it should return the area of the current Square
        """
        return self.__size * self.__size
