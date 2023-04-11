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
