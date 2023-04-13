#!/usr/bin/python3
"""Function that inserts a line of text to a file.
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """Function to search and update
    Args:
        filename (str): The file to insert text, search and update
        search_string (str): the string to search for
        new_string (str): the new string with which to update `search_string`
    Return:
        None
    """
    text = ""
    with open(filename, encoding="utf-8") as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
