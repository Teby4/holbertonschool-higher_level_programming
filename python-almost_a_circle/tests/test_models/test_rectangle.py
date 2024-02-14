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

    def test_y(self):
        """test for the y variable on rectangle"""

    def test_width(self):
        """test for the width variable on rectangle"""

    def test_height(self):
        """test for the height variable on rectangle"""

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
