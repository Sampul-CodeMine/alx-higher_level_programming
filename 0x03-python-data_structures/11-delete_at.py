#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Function to delete an element in a list at a specified index

    Args:
        my_list: List containing the integers
        idx: the index at which to delete from

    Returns:
        Returns original list if index is negative/out of range
        else returns the modified list
    """
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    else:
        del my_list[idx]
    return (my_list)
