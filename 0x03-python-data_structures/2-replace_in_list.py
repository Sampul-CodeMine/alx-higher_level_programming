#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """Function to replace element at an index in a list

    Args:
        my_list: list containing the integers to print
        idx: the index of the element
        element: number to replace the previous number

    Returns:
        Return original list if idx < 0 > len(list) else modified list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    else:
        my_list[idx] = element
        return my_list
