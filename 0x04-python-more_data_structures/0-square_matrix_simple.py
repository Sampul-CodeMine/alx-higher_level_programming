#!/usr/bin/python3

"""Function square the values of all integers in a matrix

    Args:
        matrix: the matrix to square all its value

    Returns:
        Returns a new matrix of the same size with the initial matrix
    """


def square_matrix_simple(matrix=[]):
    if matrix is None:
        return
    new_matrix = []
    for i in matrix:
        row = []
        for j in i:
            row.append(j * j)
        new_matrix.append(row)
    return (new_matrix)
