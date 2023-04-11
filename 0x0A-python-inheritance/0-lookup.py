#!/usr/bin/python3
"""Defines a function lookup."""


def lookup(obj):
    """function that returns available list of attributes and methods of an
    object
    Args:
        obj (Any): it could be a class object, list, tuple, int, str etc
    Return:
        (list) - A list of the available attributes or methods
    """
    return dir(obj)
