#!/usr/bin/python3
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

m_a = [[1, 2], [3, 4]]
m_b = [[1, 2], [3, 4, 5]]
print(lazy_matrix_mul(m_a, m_b))
