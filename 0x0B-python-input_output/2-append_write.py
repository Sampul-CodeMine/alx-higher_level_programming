#!/usr/bin/python3
"""Defines a function that appends text to already existing
contents in a file."""


def append_write(filename="", text=""):
    """Function to append contents to a file
    Args:
        filename (str): the full path to the file
        text (str): the text to be written into the file
    Return:
        None
    """
    with open(filename, mode="a", encoding="utf-8") as file_path:
        return file_path.write(text)
