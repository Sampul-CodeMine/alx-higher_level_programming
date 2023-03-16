#!/usr/bin/python3

"""Function to return a list with all elements in a list multiplied by number

    Args:
        my_list: Initial list
        number: number with which to multiply the list

    Returns:
        Returns a new list
    """


def multiply_list_map(my_list=[], number=0):
    new_list = [num*2 for num in my_list]
    return (new_list)
