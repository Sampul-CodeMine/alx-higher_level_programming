#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Function to print a list in reverse

    Args:
        my_list: list containing the integers to print

    Returns:
        Return the list in reverse with each numbers on a new line 
    """
    length = len(my_list) - 1
    count = length
    while count >= 0:
        print("{:d}".format(my_list[count]))
        count = count - 1
