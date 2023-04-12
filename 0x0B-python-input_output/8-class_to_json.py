#!/usr/bin/python3
"""Function that returns a Python class to JSON object"""


def class_to_json(obj):
    """Function to build a dictionary obj into JSON
    Args:
        obj: the object to get its dictionary structure
    Return:
        dictionary represntation of a data structure"""
    return obj.__dict__
