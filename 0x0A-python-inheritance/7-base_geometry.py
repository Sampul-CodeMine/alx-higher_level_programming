#!/usr/bin/python3
"""Defines a BaseGeometry Class"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator"""

    def area(self):
        """A public method that is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function to validate an integer passed as an argument
        Args:
            name (str): The name of the argument passed
            value (int): The argument to validate
        Raises:
            TypeError: if the datatype of `value` is not integer
            ValueError: if `value` is < or = 0 (zero)
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
