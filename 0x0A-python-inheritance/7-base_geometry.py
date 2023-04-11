#!/usr/bin/python3
"""Defines a Geometry Class"""


class BaseGeometry:
    """A class that represents a Geometric object"""

    def __init__(self):
        """Class constructor / Initializer"""
        pass

    def area(self):
        """A public method that is not implemented"""
        raise Exception(f"area() is not implemented")

    def integer_validator(self, name, value):
        """function to validate an integer passed as an argument
        Args:
            name (str): The name of the argument passed
            value (int): The argument to validate
        Raises:
            TypeError: if the datatype of `value` is not integer
            ValueError: if `value` is < or = 0 (zero)
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
