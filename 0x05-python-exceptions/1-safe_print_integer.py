#!/usr/bin/python3

def safe_print_integer(value):
    """Function to print an integer with the format specifier

    Args:
        value: the value to print

    Returns:
        True if value was printed else False
    """
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
