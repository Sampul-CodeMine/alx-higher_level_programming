#!/usr/bin/python3

def no_c(my_string):
    """Function to remove c or C from a string

    Args:
        my_string: string to check for cC and remove if found

    Returns:
        Returns a new string without the characters cC
    """
    new_str = ""
    for char in my_string:
        if char in "cC":
            new_str += ""
        else:
            new_str += char
    return (new_str)
