#!/usr/bin/python3

"""Function to return the weighted average of all integer tuples
The Tuples are structured thus:
(score, weight)
Formular:
(score * weight)/weight

    Args:
        my_list: the list containing tuples

    Returns:
        Returns 0 if list is empty else return the average
    """


def weight_average(my_list=[]):
    if my_list is None:
        return (0)
    sum_tup = 0
    sum_weight = 0
    for tup in my_list:
        sum_weight += tup[1]
        sum_tup += multiplier(tup)
    return (sum_tup / sum_weight)


def multiplier(my_tup=()):
    data = 1
    for i in my_tup:
        data *= i
    return data
