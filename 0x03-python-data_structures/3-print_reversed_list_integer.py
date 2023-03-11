#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Function to print a list in reverse

    Args:
        my_list: list containing the integers to print

    Returns:
        Return the list in reverse with each numbers on a new line
    """
    if my_list is None:
        return
    my_list.reverse()
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
