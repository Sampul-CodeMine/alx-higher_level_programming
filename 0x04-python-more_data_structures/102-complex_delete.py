#!/usr/bin/python3

"""Function to delete keys with specific values

    Args:
        a_dictionary: dictionary containing keys and values
        value: value to seach for in the dictionary

    Returns:
        Returns modified dictionary if value is found else return original
    """


def complex_delete(a_dictionary, value):
    for key in list(a_dictionary):
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
