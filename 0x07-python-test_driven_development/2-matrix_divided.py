#!/usr/bin/python3
"""Perform matrix division."""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix.
    Args:
        matrix: A list of integer or float elements (list).
        div: Number to divide with (int | float).
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix containing the result of the division.
    """
    if not isinstance(matrix, list)\
            or matrix is None\
            or not all(isinstance(row, list) for row in matrix)\
            or not all((isinstance(ele, int)
                        or isinstance(ele, float)) for ele
                       in [num for row in matrix for num in row]):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round((num / div), 2) for num in row] for row in matrix]
    return new_matrix
