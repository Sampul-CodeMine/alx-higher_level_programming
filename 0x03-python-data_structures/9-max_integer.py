#!/usr/bin/python3

def max_integer(my_list=[]):
    """Function to get the largest integer from a list of integers

    Args:
        my_list: List containing the integers to check for the biggest value

    Returns:
        Returns None if list is empty else return the biggest value
    """

    if len(my_list) == 0:
        return
    biggest = my_list[0]
    for num in range(len(my_list)):
        if biggest < my_list[num]:
            biggest = my_list[num]
    return (biggest)
