#!/usr/bin/python3

def safe_print_division(a, b):
    """Function to divide 2 integer and print the result

    Args:
        a: first value (int)
        b: second value (int)

    Returns:
        None if unsuccessful else the result
    """
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
