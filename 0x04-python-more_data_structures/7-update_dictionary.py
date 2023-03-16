#!/usr/bin/python3

"""Function to update a dictionary:
If the key exists, it updates or replaces the value.
If the key does not exist, it creates that key and assigns a value.

    Args:
        a_dictionary: the specified dictionary
        key: the key to look for
        value: the value to replace the old value or insert as new

    Returns:
        Returns an updated / modified dictionary
    """


def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return (a_dictionary)
