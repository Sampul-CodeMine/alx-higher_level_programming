#!/usr/bin/python3

"""Function to print a sorted dictionary

    Args:
        a_dictionary: the specified dictionary

    Returns:
        Returns a sorted dictionary
    """


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
