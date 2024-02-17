#!/usr/bin/python3
"""
test file
"""

import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
        test cases for Rectangle class
    """

    def test_x(self):
        """test for the x variable on rectangle"""
        obj = Base(x=36)
        self.assertEqual(obj.x, 36)
        with self.assertRaises(TypeError):
            x([1, "3"])
        with self.assertRaises(ValueError):
            x(-9)

    def test_y(self):
        """test for the y variable on rectangle"""
        obj = Base(y=36)
        self.assertEqual(obj.y, 36)
        with self.assertRaises(TypeError):
            y([1, "4"])
        with self.assertRaises(ValueError):
            y(-8)

    def test_width(self):
        """test for the width variable on rectangle"""
        obj = Base(width=36)
        self.assertEqual(obj.width, 36)
        with self.assertRaises(TypeError):
            width([1, "5"])
        with self.assertRaises(ValueError):
            width(-6)

    def test_height(self):
        """test for the height variable on rectangle"""
        obj = Base(height=35)
        self.assertEqual(obj.height, 35)
        with self.assertRaises(TypeError):
            height([1, "10"])
        with self.assertRaises(ValueError):
            height(-4)

    def test_id(self):
        """ test for id variable on Rectangle"""
        obj = Base(id=35)
        self.assertEqual(obj.id, 35)
        obj = Base(id=0)
        self.assertEqual(obj.id, 0)
        obj = Base(id=-35)
        self.assertEqual(obj.id, -35)

        Base._Base__nb_objects = 0
        obj = Base()
        self.assertEqual(obj.id, 1)
        obj = Base()
        self.assertEqual(obj.id, 2)
        obj = Base()
        self.assertEqual(obj.id, 3)

if __name__ == "__main__":
    unittest.main()
