#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

m_a = [
    [1, 2],
    [2, 3]
]
m_b = [
    [1, 3],
    [2, 2],
    [4, 2]
]
try:
    print(matrix_mul())
except Exception as e:
    print(e)