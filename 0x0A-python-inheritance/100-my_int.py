#!/usr/bin/python3
"""Defines the class MyInt"""


class MyInt(int):
    """Class that negates the actual version of the integer Baseclass.
    A rebel version of an integer, perfect for opposite day!"""
    def __new__(cls, *args, **kwargs):
        """create a new instance of the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """this magic method turns == to !="""
        return int(self) != other

    def __ne__(self, other):
        """this magic method turns != to =="""
        return int(self) == other
