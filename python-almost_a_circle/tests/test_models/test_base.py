#!/usr/bin/python3
"""
test file
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """
        test cases for base class
    """

    def test_init_(self):
        """ test for init function on base"""
        
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
