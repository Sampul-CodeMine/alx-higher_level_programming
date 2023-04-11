#!/usr/bin/python3
"""Defines a function that checks type of object."""


def is_same_class(obj, a_class):
    """Function to check if an object passed is exactly an instance of the
    specified class passed also as an argument.

    Args:
        obj (any): The object to check its type.
        a_class (type): The class to match the type `obj` to.
    Returns:
        True (bool) if `obj` is exactly an instance of `a_class`
        False (bool) if `obj` is not an instance of `a_class`
    """
    return True if type(obj) == a_class else False
