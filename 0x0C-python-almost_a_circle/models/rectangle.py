#!/usr/bin/python3
"""This Defines the `Rectangle` Class for the Project
The `Rectangle` class is a subclass to the `Base` class
"""

from models.base import Base


class Rectangle(Base):
    """This is a class that represents a Rectangle object"""

    def __init__(self, width: int, height: int, x=0, y=0, id=None):
        """Initialization of a new Rectangle object"""
        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value: int):
        """Set the width of the Rectangle.
        Args:
            value (int): value is of type integer
        Raises:
            ValueError: if the value passed is < or = 0
            TypeError: if the value passed is not of type integer
        """
        if type(value) == int:
            if value > 0:
                self.__width = value
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """Get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle.
        Args:
            value (int): value is of type integer
        Raises:
            ValueError: if the value passed is < or = 0
            TypeError: if the value passed is not of type integer
        """
        if type(value) == int:
            if value > 0:
                self.__height = value
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """Get the x of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set the x coordinates of the Rectangle.
        Args:
            value (int): value is of type integer
        Raises:
            ValueError: if the value passed is < 0
            TypeError: if the value passed is not of type integer
        """
        if type(value) == int:
            if value >= 0:
                self.__x = value
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError("x must be an integer")

    @property
    def y(self):
        """Get the y coordinates of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y of the Rectangle.
        Args:
            value (int): value is of type integer
        Raises:
            ValueError: if the value passed is < or = 0
            TypeError: if the value passed is not of type integer
        """
        if type(value) == int:
            if value >= 0:
                self.__y = value
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("y must be an integer")
