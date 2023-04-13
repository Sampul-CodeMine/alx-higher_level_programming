#!/usr/bin/python3
"""Function that defines a Pascal's Triangle."""


def pascal_triangle(n):
    """Represent Pascal's Triangle
    Args:
        n (int): the size of the triangle.
    Return:
        list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    p_triangle = []
    p_triangle.append([1])
    while len(p_triangle) != n:
        ele = p_triangle[-1]
        holder = [1]
        for i in range(len(ele) - 1):
            holder.append(ele[i] + ele[i + 1])
        holder.append(1)
        p_triangle.append(holder)
    return p_triangle
