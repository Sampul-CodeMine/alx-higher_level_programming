#!/usr/bin/python3
"""This Defines the `Rectangle` Class for the Project
The `Rectangle` class is a subclass to the `Base` class
"""

from models.base import Base


class Rectangle(Base):
    """This is a class that represents a Rectangle object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialization of a new Rectangle object"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @staticmethod
    def set_validation(attrib, value: int):
        """Class static method that validates a value for its data type
        and its value else raisesan exception"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attrib))
        if attrib == "x" or attrib == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attrib))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attrib))

    @property
    def width(self):
        """Get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle.
        Args:
            value (int): value is of type integer
        Raises:
            ValueError: if the value passed is < or = 0
            TypeError: if the value passed is not of type integer
        """
        self.set_validation("width", value)
        self.__width = value

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
        self.set_validation("height", value)
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the Rectangle."""
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
        self.set_validation("x", value)
        self.__x = value

    @property
    def y(self):
        """Get the y coordinates of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set the y coordinates of the Rectangle.
        Args:
            value (int): value is of type integer
        Raises:
            ValueError: if the value passed is < 0
            TypeError: if the value passed is not of type integer
        """
        self.set_validation("y", value)
        self.__y = value
