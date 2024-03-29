#!/usr/bin/python3
"""This is a class that creates a Rectangle Object when instantiated"""


class Rectangle:
    """This class represents a Rectangle object"""
    def __init__(self, width=0, height=0):
        """Default constructor or initializer for the class
        Args:
            width: The width of the rectangle object (int)
            height: The height of the rectangle object (int)
        """
        self.__width = width
        self.__height = height

    """Getter and setter for the Width property"""
    @property
    def width(self):
        """Get the width of the rectangle object"""
        if (not isinstance(self.__width, int)) or isinstance(self.__width,
                                                             bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, new_value):
        """Sets the value of the width for the rectangle"""
        if not isinstance(new_value, int):
            raise TypeError("width must be an integer")
        if new_value < 0:
            raise ValueError("width must be >= 0")
        self.__width = new_value

    """Getter and setter for the Height property"""
    @property
    def height(self):
        """Get the height of the rectangle object"""
        if (not isinstance(self.__height, int))\
                or isinstance(self.__height, bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, new_value):
        """Sets the value of the height for the rectangle"""
        if not isinstance(new_value, int):
            raise TypeError("height must be an integer")
        if new_value < 0:
            raise ValueError("height must be >= 0")
        self.__height = new_value
    
    """Method to calculate the area of the rectangle"""
    def area(self):
        try:
            self.__width = int(self.__width)
            self.__height = int(self.__height)
            return self.__width * self.__height
        except (ValueError, TypeError):
            raise TypeError("value must be an integer")

    """Method to calculate the perimeter of the rectangle"""
    def perimeter(self):
        try:
            self.__width = int(self.__width)
            self.__height = int(self.__height)
            if self.__width > 0 or self.__height > 0:
                return (self.__width * 2) + (self.__height * 2)
        except (ValueError, TypeError):
            raise TypeError("value must be an integer")
        return 0
