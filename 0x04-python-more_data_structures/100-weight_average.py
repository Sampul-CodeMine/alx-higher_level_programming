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
    if my_list is None or my_list == []:
        return (0)
    sum_score = 0
    sum_weight = 0
    for score, weight in my_list:
        sum_weight += weight
        sum_score += score * weight
    return (sum_score / sum_weight)
