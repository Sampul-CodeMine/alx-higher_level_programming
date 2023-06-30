#!/usr/bin/python3
"""This is a Module containing a function that finds a peak
from an unsorted list"""


def find_peak(numlist: list):
    """Function to find the peak from an unsorted list of integers
    Args:
        numlist (list): the list of unsorted integers
    Return:
        (int) - the peak number
    """
    if type(numlist) is not list:
        return None
    if numlist == [] or numlist is None:
        return None

    """get the length of the list"""
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

    """get half of middle of the list"""
    half = int(((num_len - 0) // 2) + 0)

    if ((numlist[half] >= numlist[half - 1]) and
            (numlist[half] >= numlist[half + 1])):
        return (numlist[half])

    if ((half > 0) and (numlist[half] < numlist[half + 1])):
        return (find_peak(numlist[half:]))

    if ((half > 0) and (numlist[half] < numlist[half - 1])):
        return (find_peak(numlist[:half]))
