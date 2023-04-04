#!/usr/bin/python3
"""Class that defines a locked class."""


class LockedClass:
    """Only allows instantiation of new LockedClass object
    for attribute file_name
    """
    __slots__ = ["first_name"]
