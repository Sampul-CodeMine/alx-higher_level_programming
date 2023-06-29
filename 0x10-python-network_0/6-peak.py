#!/usr/bin/python3
"""This is a Module containing a function that finds a peak
from an unsorted list"""


def find_peak(list_of_integers: list) -> int | None:
    """Function to find the peak from an unsorted list of integers

    Args:
        list_of_integers (list): the list of unsorted integers

    Return:
        ...
    """
    if type(list_of_integers) is not list:
        return None

    num_len = len(list_of_integers)
    if num_len == 0:
        return None
    if num_len == 1:
        return (list_of_integers[0])
    if num_len == 2:
        if list_of_integers[0] >= list_of_integers[1]:
            return (list_of_integers[0])
        else:
            return (list_of_integers[1])
    for i in range(num_len):
        v = list_of_integers[i]
        if ((i > 0 and i < (num_len - 1)) and (list_of_integers[i + 1] <= v)
                and (list_of_integers[i - 1] <= v)):
            return v
        elif i == 0 and list_of_integers[i + 1] <= v:
            return (v)
        elif i == (num_len - 1) and list_of_integers[i - 1] <= v:
            return (v)
    return None
