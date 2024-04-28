#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from importlib import import_module

# Importing the max_integer function from the 6-max_integer module
max_integer_module = import_module("6-max_integer")
max_integer = max_integer_module.max_integer

class TestMaxInteger(unittest.TestCase):
    def test_positive_integers(self):
        """Test with a list containing positive integers."""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_negative_integers(self):
        """Test with a list containing negative integers."""
        result = max_integer([-1, -2, -3, -4])
        self.assertEqual(result, -1)

    def test_mixed_integers(self):
        """Test with a list containing both positive and negative integers."""
        result = max_integer([-1, 2, -3, 4])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test with an empty list."""
        result = max_integer([])
        self.assertIsNone(result)

    def test_single_integer(self):
        """Test with a list containing only one integer."""
        result = max_integer([5])
        self.assertEqual(result, 5)

    def test_floats(self):
        """Test with a list containing floats."""
        result = max_integer([1.5, 2.5, 3.5, 4.5])
        self.assertEqual(result, 4.5)

    def test_mixed_numbers(self):
        """Test with a list containing a mix of integers and floats."""
        result = max_integer([1, 2.5, 3, 4.5])
        self.assertEqual(result, 4.5)

    def test_edge_case_large_numbers(self):
        """Test with a list containing large integers."""
        result = max_integer([1000000, 2000000, 3000000])
        self.assertEqual(result, 3000000)

    def test_edge_case_min_integer(self):
        """Test with a list containing the minimum integer value."""
        result = max_integer([-2147483648, 0, 2147483647])
        self.assertEqual(result, 2147483647)

    def test_edge_case_max_integer(self):
        """Test with a list containing the maximum integer value."""
        result = max_integer([2147483647, 0, -2147483648])
        self.assertEqual(result, 2147483647)

    def test_edge_case_max_float(self):
        """Test with a list containing the maximum float value."""
        result = max_integer([1e100, 2e100, 3e100])
        self.assertEqual(result, 3e100)

if __name__ == '__main__':
    unittest.main()
