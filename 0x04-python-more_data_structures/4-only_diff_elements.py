#!/usr/bin/python3

"""Function to return a set of elements present in only one set

    Args:
        set_1: first set containing values
        set_2: second set containing values

    Returns:
        Returns a list of elements in only one set
    """


def only_diff_elements(set_1, set_2):
    return (set_1.symmetric_difference(set_2))
