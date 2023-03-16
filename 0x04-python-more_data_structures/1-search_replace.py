#!/usr/bin/python3

"""Function to replace all occurences of an element by another in a new list

    Args:
        my_list: the list to search through
        search: the element to search for in the list
        replace: the value to replace the searched item or element

    Returns:
        Returns a new list with modified elements
    """


def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_my_list = []
    for i in range(len(my_list)):
        if search == my_list[i]:
            new_my_list.append(replace)
        else:
            new_my_list.append(my_list[i])
    return (new_my_list)
