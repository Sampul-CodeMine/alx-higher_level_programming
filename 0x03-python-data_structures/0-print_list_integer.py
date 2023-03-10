#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Function to print list integers

    Args:
        my_list: list containing the integers to print

    Returns:
        Return nothing but prints intgers on separate lines
    """
    for num in my_list:
        print("{:d}".format(num))
