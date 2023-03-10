#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Function to replace element at an index in a copied list
    without modifying the original list

    Args:
        my_list: list containing the integers to print
        idx: the index of the element
        element: number to replace the previous number

    Returns:
        Return copy of the original list if idx < 0 > len(list) else
        print modified copy of the list
    """
    temp_list_copy = my_list.copy()
    if idx < 0 or idx > len(my_list) - 1:
        return my_list.copy()
    else:
        temp_list_copy[idx] = element
        return temp_list_copy
