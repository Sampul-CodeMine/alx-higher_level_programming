#!/usr/bin/python3
"""Defines a function that writes an Object to a textfile using JSON repr"""
import json


def save_to_json_file(my_obj, filename):
    """Function that converts a python object into JSON string and
    save it to a file
    Args:
        my_obj (Any): python object
        filename (str): the full path to the file to write to
    Return:
        None
    """
    with open(filename, mode="w", encoding="utf-8") as file_path:
        json.dump(my_obj, file_path)
