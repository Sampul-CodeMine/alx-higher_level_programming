#!/usr/bin/python3
"""This is a Module containing a function that finds a peak
from an unsorted list"""


def find_peak(numlist: list) -> int | None:
    """Function to find the peak from an unsorted list of integers

    Args:
        numlist (list): the list of unsorted integers

    Return:
        ...
    """
    if type(numlist) is not list:
        return None
    if numlist == [] or numlist is None:
        return None

    num_len = len(numlist)
    if num_len == 0:
        return None
    if num_len == 1:
        return (numlist[0])
    if num_len == 2:
        if numlist[0] >= numlist[1]:
            return (numlist[0])
        else:
            return (numlist[1])
    half = num_len // 2
    if (half - 1) < 0 and (half + 1) >= num_len:
        return (numlist[half])
    elif (half - 1) < 0:
        if (numlist[half] > numlist[half + 1]):
            return numlist[half]
        else:
            return numlist[half + 1]
    elif (half + 1) >= num_len:
        if (numlist[half] > numlist[half - 1]):
            return numlist[half]
        else:
            return numlist[half - 1]
    if numlist[half - 1] < numlist[half] > numlist[half + 1]:
        return numlist[half]
    if numlist[half + 1] > numlist[half - 1]:
        return find_peak(numlist[half:])
    return find_peak(numlist[:half])
