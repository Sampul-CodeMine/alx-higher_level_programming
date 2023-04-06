#!/usr/bin/python3
"""Unittest class for max_integer([..]) function."""
import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerObj(unittest.TestCase):
    """This class defines unittest for the max_integer([...]) method"""

    def test_for_empty_strings(self):
        """Test if the parameter is an empty string"""
        self.assertEqual(max_integer(""), None)

    def test_for_a_string(self):
        """Test if the parameter is a string"""
        self.assertEqual(max_integer("example"), 'x')

    def test_for_list_of_strings(self):
        """Test if the parameter is a list of strings"""
        self.assertEqual(max_integer(["example", "sample", "test", "instance"]), 'test')

    def test_list_with_int_and_float(self):
        """Test a list of ints and floats."""
        self.assertEqual(max_integer([12, 2.5, 14.2, 5, 7, 13]), 14.2)

    def test_list_with_float(self):
        """Test a list of floats."""
        self.assertEqual(max_integer([2.2, 2.4, 0.4, -10.1, 7.7]), 7.7)

    def test_single_element_list(self):
        """Test a single element list"""
        self.assertEqual(max_integer([2]), 2)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_sorted_list(self):
        """Test a sorted list either ascending or descending"""
        self.assertEqual(max_integer([1, 3, 4, 6, 8, 12]), 12)
        self.assertEqual(max_integer([11, 9, 8, 4, 2, 0]), 11)

    def test_scattered_list(self):
        """Test an unsorted list"""
        self.assertEqual(max_integer([12, 443, 54, 900, 324, -1000]), 900)

    def test__docstring(self):
        """Tests for module docstring"""
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

    def test_function_docstring(self):
        """Tests for function docstring"""
        self.assertTrue(len(max_integer.__doc__) > 1)

if __name__ == "__main__":
    unittest.main()
