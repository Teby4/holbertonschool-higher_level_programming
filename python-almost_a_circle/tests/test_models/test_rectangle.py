import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    """
    Test cases for Rectangle class
    """

    def test_constructor_and_getters(self):
        """Test constructor and getters for Rectangle"""
        # Test case 1: Rectangle with width=5, height=10, x=2, y=3, and id=1
        rectangle1 = Rectangle(width=5, height=10, x=2, y=3, id=1)
        self.assertEqual(rectangle1.width, 5)
        self.assertEqual(rectangle1.height, 10)
        self.assertEqual(rectangle1.x, 2)
        self.assertEqual(rectangle1.y, 3)
        self.assertEqual(rectangle1.id, 1)

        # Test case 2: Rectangle with default values
        rectangle2 = Rectangle(width=0, height=0)
        self.assertEqual(rectangle2.width, 0)
        self.assertEqual(rectangle2.height, 0)
        self.assertEqual(rectangle2.x, 0)
        self.assertEqual(rectangle2.y, 0)
        self.assertEqual(rectangle2.id, 2)

    def test_setters(self):
        """Test setters for Rectangle"""
        # Test case 1: Setting new values for width, height, x, and y
        rectangle1 = Rectangle(width=5, height=10, x=2, y=3)
        rectangle1.width = 8
        rectangle1.height = 15
        rectangle1.x = 4
        rectangle1.y = 6

        self.assertEqual(rectangle1.width, 8)
        self.assertEqual(rectangle1.height, 15)
        self.assertEqual(rectangle1.x, 4)
        self.assertEqual(rectangle1.y, 6)

        # Test case 2: Setting new values for width, height, x, and y with negative values
        rectangle2 = Rectangle(width=5, height=10, x=2, y=3)
        rectangle2.width = 12
        rectangle2.height = -7
        rectangle2.x = -1
        rectangle2.y = 0

        self.assertEqual(rectangle2.width, 12)
        self.assertEqual(rectangle2.height, -7)
        self.assertEqual(rectangle2.x, -1)
        self.assertEqual(rectangle2.y, 0)

if __name__ == "__main__":
    unittest.main()