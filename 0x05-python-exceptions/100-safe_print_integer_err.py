#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Function to print an integer with format {:d}
    If a ValueError occurs, an error message is printed to stderr

    Args:
        value: The integer to print (int)

    Returns:
        Returns True if successful, else False if a TypeError or ValueError
    occurs 
    """
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
