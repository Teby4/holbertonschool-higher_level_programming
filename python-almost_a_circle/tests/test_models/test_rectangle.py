import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_init(self):
        r = Rectangle(10, 20, 1, 2, 3)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 3)

    def test_area(self):
        r = Rectangle(5, 5)
        self.assertEqual(r.area(), 25)

    def test_display(self):
        r = Rectangle(3, 2)
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as fake_out:
            r.display()
            self.assertEqual(fake_out.getvalue(), "###\n###\n")

    def test_str(self):
        r = Rectangle(5, 5, 1, 1, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 1/1 - 5/5")

    def test_update(self):
        r = Rectangle(1, 1, 1, 1, 1)
        r.update(2, 2, 2, 2, 2)
        self.assertEqual(r.id, 2)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 2)

if __name__ == '__main__':
    unittest.main()