#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Function to print a matrix of integers

    Args:
        matrix: The matrix to print its rows and columns

    Returns:
        Returns the integers in a matrix
    """
    for row in matrix:
        for j in row:
            if row[-1] != j:
                print("{:d}".format(j), end=" ")
            else:
                print("{:d}".format(j), end="")
        print()
    pass
