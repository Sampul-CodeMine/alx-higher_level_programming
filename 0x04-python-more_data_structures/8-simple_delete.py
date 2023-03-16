#!/usr/bin/python3

"""Function to delete a key from a dictionary

    Args:
        a_dictionary: the specified dictionary
        key: the key to look for

    Returns:
        Returns an updated / modified dictionary
    """


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return (a_dictionary)
