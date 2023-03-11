#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Function to find the multiple of 2 in a list of integers

    Args:
        my_list: List containing the integers

    Returns:
        Returns None if list is empty else return the biggest value
    """
    # list_bool = []
    # for i in range(len(my_list)):
    #     if my_list[i] % 2 == 0:
    #         list_bool.append(True)
    #     else:
    #         list_bool.append(False)
    # return (list_bool)
    #
    # using list comprehension
    list_bool = [True if (my_list[i] % 2 == 0) 
                 else False for i in range(len(my_list))]
    return (list_bool)