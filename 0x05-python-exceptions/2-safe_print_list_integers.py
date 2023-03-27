#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Function to print the first x integer elements from a list.

    Args:
        my_list: The list to print elements from (list).
        x: The number of elements to print from my_list (int).

    Returns:
        The number of elements printed.
    """
    count = 0
    for itr in range(x):
        try:
            print("{:d}".format(my_list[itr]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return count
