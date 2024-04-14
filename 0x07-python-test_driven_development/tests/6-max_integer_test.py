#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest test cases for max_integer"""

    def test_docstr(self):
        # Tests for docstring in module and function
        M = __import__('6-max_integer').__doc__
        f = max_integer.__doc__
        self.assertTrue(len(M) > 1)
        self.assertTrue(len(f) > 1)

    def test_success(self):
        # Test for success in order
        self.assertEqual(max_integer([2, 5, 1, 0]), 5)
        self.assertEqual(max_integer([2, 3, 1, 5]), 5)
        self.assertEqual(max_integer([5, 2, 3, 1]), 5)

        # Test for equal numbers
        self.assertEqual(max_integer([2, 2, 2]), 2)

        # Test for 0
        self.assertEqual(max_integer([0, 0, 0]), 0)

        # Test for empty list
        self.assertIsNone(max_integer([]))

        # Test for No args
        self.assertIsNone(max_integer())

        # Test for single element
        self.assertEqual(max_integer([9]), 9)

        # Test for a negative
        self.assertEqual(max_integer([-1, 4, 6]), 6)

        # Test for all negatives
        self.assertEqual(max_integer([-1, -4, -3]), -1)

    def test_raises(self):
        self.assertRaises(TypeError, max_integer, 98)
        self.assertRaises(TypeError, max_integer, [2, 1, 5, "Test", 2])


if __name__ == "__main__":
    unittest.main()
