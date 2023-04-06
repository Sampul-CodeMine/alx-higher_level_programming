#!/usr/bin/python3
"""Function to print a square with the character # """


def print_square(size: int):
    """This is a function that accepts an integer parameter as the size of a
    a square and prints out the dimension of the square (length = size and
    width = size)
    Args:
        size: the size of the square (int)
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size >= 0:
        for itr in range(size):
            for j in range(size):
                print("#", end="")
            print("")
    else:
        raise ValueError("size must be >= 0")
