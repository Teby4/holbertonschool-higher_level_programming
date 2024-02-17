#!/usr/bin/python3
"""
test file
"""


import unittest
from models.rectangle import Rectangle
import io
import unittest.mock


class TestRectangle(unittest.TestCase):
    """
    Test cases for Rectangle class
    """

    def test_constructor_and_getters(self):
        """Test constructor and getters for Rectangle"""
        # Test case 1: Rectangle with valid parameters
        rectangle1 = Rectangle(width=5, height=10, x=2, y=3, id=1)
        self.assertEqual(rectangle1.width, 5)
        self.assertEqual(rectangle1.height, 10)
        self.assertEqual(rectangle1.x, 2)
        self.assertEqual(rectangle1.y, 3)
        self.assertEqual(rectangle1.id, 1)

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

    def test_area(self):
        """Test the area method of Rectangle"""
        # Test case 1: Rectangle with width=5 and height=10
        rectangle1 = Rectangle(width=5, height=10)
        self.assertEqual(rectangle1.area(), 50)

        # Test case 2: Rectangle with width=7 and height=3
        rectangle2 = Rectangle(width=7, height=3)
        self.assertEqual(rectangle2.area(), 21)

        # Test case 3: Rectangle with width=0 and height=15
        rectangle3 = Rectangle(width=0, height=15)
        self.assertEqual(rectangle3.area(), 0)

        # Test case 4: Rectangle with width=1 and height=1
        rectangle4 = Rectangle(width=1, height=1)
        self.assertEqual(rectangle4.area(), 1)

    def test_str_method(self):
        """Test the __str__ method of Rectangle"""
        # Test case 1: Rectangle with custom values
        rectangle1 = Rectangle(width=5, height=10, x=2, y=3, id=1)
        self.assertEqual(str(rectangle1), "[Rectangle] (1) 2/3 - 5/10")

    def test_update_method(self):
        """Test the update method of Rectangle"""
        # Test case 1: Update with all arguments
        rectangle = Rectangle(1, 2, 3, 4, 5)
        rectangle.update(6, 7, 8, 9, 10)
        self.assertEqual(rectangle.id, 6)
        self.assertEqual(rectangle.width, 7)
        self.assertEqual(rectangle.height, 8)
        self.assertEqual(rectangle.x, 9)
        self.assertEqual(rectangle.y, 10)


if __name__ == "__main__":
    unittest.main()
