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
    with open(filename, mode='r+', encoding="utf-8") as file_path:
        lines = file_path.readlines()
        itr = 0
        for line in lines:
            if not line.find(search_string) == -1:
                lines.insert(itr + 1, new_string)
            itr += 1
        file_path.seek(0)
        file_path.write("".join(lines))
