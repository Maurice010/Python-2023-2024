import unittest
from rectangle import *

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(1, 2, 5, 6)
        self.r2 = Rectangle(-1, 2, -4, -6)

    def test_print(self):
        self.assertEqual(str(self.r1), "[(1, 2), (5, 6)]")
        self.assertEqual(repr(self.r1), "Rectangle(1, 2, 5, 6)")

    def test_cmp(self):
        self.assertTrue(self.r1 == Rectangle(1, 2, 5, 6))
        self.assertTrue(self.r1 != self.r2)

    def test_center(self):
        self.assertEqual(self.r1.center(), Point(3, 4))
        self.assertEqual(self.r2.center(), Point(-2.5, -2))
    
    def test_area(self):
        self.assertEqual(self.r1.area(), 16)
        self.assertEqual(self.r2.area(), 24)

    def test_move(self):
        self.assertEqual(self.r1.move(1, 2), Rectangle(2, 4, 6, 8))
        self.assertEqual(self.r2.move(1, 2), Rectangle(0, 4, -3, -4))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()