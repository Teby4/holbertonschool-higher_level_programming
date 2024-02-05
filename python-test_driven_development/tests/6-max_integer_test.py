#!/usr/bin/python3
"""
Unittest max integrer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    class to test the max integrer function
    """

    def test_max(self):
        """ tests for the max integrer function"""
        self.assertEqual(max_integer([1, 10]), 10)
        self.assertEqual(max_integer([1, -1]), 1)
        self.assertEqual(max_integer([15, 10]), 15)
        self.assertEqual(max_integer([20, 10]), 20)
        self.assertEqual(max_integer([-1, -2]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 1.5]), 1.5)
        with self.assertRaises(TypeError):
            max_integer([1, "10"])
        with self.assertRaises(TypeError):
            max_integer(None)
