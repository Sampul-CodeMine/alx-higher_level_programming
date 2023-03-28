#!/usr/bin/python3
"""Creating a class Square"""


class Square:
    """Representation of a Square object"""

    def __init__(self, size=0):
        """__init__ is a default constructor for the Square class
        Args:
            size: (int) defines the size of the Square object to be created.
        """
        self.__size = size

    @property
    def size(self):
        """Getter for the size attribute/property for the Square class"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size attribute/property for the Square class"""
        if isinstance(value, int):
            if value >= 0:
                self.__size = value
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

    def my_print(self):
        """Function to print the square
        It prints out the square as an object using the # symbol
        """
        if self.__size == 0:
            print("")
        for itr in range(0, self.__size):
            for itr in range(self.__size):
                print("#", end="")
            print("")
