#!/usr/bin/python3
"""Defines a function that converts python object to JSON."""
import json


def to_json_string(my_obj):
    """function to return JSON representation of a string object.
    Args:
        my_obj (Any): a python object to be converted into JSON
    Return:
        The JSON format of `my_obj`
    """
    return json.dumps(my_obj)
