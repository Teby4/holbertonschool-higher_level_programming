#!/usr/bin/python3
"""
test file
"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    Test cases for Rectangle class
    """

    def test_constructor(self):
        """Test constructor for Rectangle"""
        # Test case 1: Rectangle with valid parameters
        rectangle1 = Rectangle(width=5, height=10, x=2, y=3, id=1)
        self.assertEqual(rectangle1.width, 5)
        self.assertEqual(rectangle1.height, 10)
        self.assertEqual(rectangle1.x, 2)
        self.assertEqual(rectangle1.y, 3)
        self.assertEqual(rectangle1.id, 1)

        # Test case 2: Rectangle with invalid parameters
        with self.assertRaises(TypeError):
            Rectangle(width="invalid", height=10, x=2, y=3, id=1)

        with self.assertRaises(ValueError):
            Rectangle(width=-5, height=10, x=2, y=3, id=1)

    def test_setters(self):
        """Test setters for Rectangle"""
        # Test case 1: Setting valid values for width, height, x, and y
        rectangle1 = Rectangle(width=5, height=10, x=2, y=3, id=1)
        rectangle1.width = 8
        rectangle1.height = 15
        rectangle1.x = 4
        rectangle1.y = 6

        self.assertEqual(rectangle1.width, 8)
        self.assertEqual(rectangle1.height, 15)
        self.assertEqual(rectangle1.x, 4)
        self.assertEqual(rectangle1.y, 6)

        # Test case 2: Setting invalid values for width, height, x, and y
        with self.assertRaises(TypeError):
            rectangle1.width = "invalid"

        with self.assertRaises(ValueError):
            rectangle1.height = -7

        with self.assertRaises(TypeError):
            rectangle1.x = "invalid"

        with self.assertRaises(ValueError):
            rectangle1.y = -2


if __name__ == "__main__":
    unittest.main()
