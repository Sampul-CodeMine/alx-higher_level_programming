#!/usr/bin/python3

"""Function to return a new dictionary with all elements multiplied by 2

    Args:
        a_dictionary: the specified dictionary

    Returns:
        Returns a new dictionary
    """


def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for k, v in new_dict.items():
        new_dict[k] = v * 2
    return (new_dict)
