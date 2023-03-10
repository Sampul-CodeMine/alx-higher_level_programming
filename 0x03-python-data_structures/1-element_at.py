#!/usr/bin/python3

def element_at(my_list, idx):
    """Function to retrieve an integers at an index in a list

    Args:
        my_list: list containing the integers
        indx: the index of the integer to print

    Returns:
        Return None if ind < 0 > length of list else the integer at the index
    """
    if idx < 0 or idx > len(my_list) - 1:
        return
    return my_list[idx]
