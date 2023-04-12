#!/usr/bin/python3
"""Defines a function that converts JSON object to python object."""
import json


def from_json_string(my_str):
    """function to return dictionary representation of a JSON object.
    Args:
        my_str (Any): a JSON string to be converted into python dictionary
    Return:
        A python dictionary of `my_str`
    """
    return json.loads(my_str)
