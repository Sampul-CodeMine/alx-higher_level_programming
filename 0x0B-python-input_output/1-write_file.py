#!/usr/bin/python3
"""Defines a function that writes text to a file."""


def write_file(filename="", text=""):
    """Function to write contents to a file
    Args:
        filename (str): the full path to the file
        text (str): the text to be written into the file
    Return:
        None
    """
    with open(filename, mode="w", encoding="utf-8") as file_path:
        return file_path.write(text)
