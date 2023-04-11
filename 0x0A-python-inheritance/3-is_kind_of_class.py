#!/usr/bin/python3
"""Defines a function that checks  if the object is an instance of, or if the
object is an instance of a class that inherited from, the specified class."""


def is_kind_of_class(obj, a_class):
    """Function to check if an object passed is an instance or object of an
    instance inherited from a specified class

    Args:
        obj (any): The object to check its type.
        a_class (type): The class to match the type `obj` to.
    Returns:
        True (bool) if `obj` is an instance of `a_class`
        False (bool) if `obj` is not an instance of `a_class`
    """
    return True if isinstance(obj, a_class) else False
