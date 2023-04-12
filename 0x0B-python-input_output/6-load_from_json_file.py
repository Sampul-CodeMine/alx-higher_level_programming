#!/usr/bin/python3
"""Defines a function reads from a JSON file"""
import json


def load_from_json_file(filename):
    """Function that reads a string stream from a JSON file and returns
    a python dictionary object
    Args:
        filename (str): the full path to the file to load from
    Return:
        (dict) - A python dictionary object
    """
    with open(filename, mode="r", encoding="utf-8") as file_path:
        return json.load(file_path)
