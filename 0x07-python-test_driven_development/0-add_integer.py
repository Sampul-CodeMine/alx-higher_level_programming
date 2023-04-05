#!/usr/bin/python3
"""Integer addition function."""


def add_integer(a, b=98):
    """Function to perform integer addition on two (2) variables a and b.
    Float arguments are cast into ints before addition is performed.
    Args:
        a: first value (int | float)
        b: second value (int | float)
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    Returns:
        Integer result from the addition of a and b
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
