#!/usr/bin/python3
"""Defines a function that reads text from a file."""


def read_file(filename=""):
    """Function to read the contents in a file and output the
    contents to the Standard Output
    Args:
        filename (str): the full path to the file
    Return:
        None
    """
    with open(filename, mode="r", encoding="utf-8") as file_path:
        print(file_path.read(), end="")
