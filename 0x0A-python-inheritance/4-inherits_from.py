#!/usr/bin/python3
"""Defines a function that checks if an object is has direct or indirect
inheritance from the specified class."""


def inherits_from(obj, a_class):
    """Function to check if an object is a subclass of a class

    Args:
        obj (any): The object to check its inheritance.
        a_class (type): The class to match the type `obj` to.
    Returns:
        True (bool) if `obj` is subclass of `a_class`
        False (bool) if `obj` is not a subclass of `a_class`
    """
    return True if issubclass(type(obj), a_class) and\
        type(obj) != a_class else False
