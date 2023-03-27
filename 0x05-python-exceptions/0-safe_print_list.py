#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Function to print x number of elements from a list.

    Args:
        my_list: The list to print elements from (list).
        x: The number of elements to print from my_list (int).

    Returns:
        The number of elements printed.
    """
    if my_list == []:
        return
    count = 0
    while True:
        try:
            if count < x:
                print("{}".format(my_list[count]), end="")
                count += 1
            else:
                print()
                return count
        except IndexError:
            print()
            return count
