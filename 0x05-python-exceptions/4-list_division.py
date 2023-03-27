#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """Function to divide elements by elements of 2 lists

    Args:
        my_list_1: first list (list)
        my_list_2: second lsit (list)
        list_length: number of elements to divide (int)

    Returns:
        new list with length list_length containing products of both
        list elements
    """
    list_new = []
    l_div = 0
    for itr in range(0, list_length):
        try:
            l_div = my_list_1[itr] / my_list_2[itr]
        except IndexError:
            print("out of range")
            l_div = 0
        except ZeroDivisionError:
            print("division by zero")
            l_div = 0
        except TypeError:
            print("wrong type")
            l_div = 0
        finally:
            list_new.append(l_div)
    return list_new
