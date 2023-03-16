#!/usr/bin/python3

"""Function to add all unique integers in a list

    Args:
        my_list: the list with integers

    Returns:
        Returns the sum
    """


def uniq_add(my_list=[]):
    if my_list is None:
        return
    sum = 0
    vals = set(my_list)
    for i in vals:
        sum += i
    return (sum)
