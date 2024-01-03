import unittest
from points import *

class TestPoint(unittest.TestCase):

    def setUp(self):
        self.p1 = Point(1, 2)
        self.p2 = Point(-2, 4)
        self.p3 = Point(3, 5)

    def test_print(self):
        self.assertEqual(str(self.p1), "(1, 2)")
        self.assertEqual(repr(self.p1), "Point(1, 2)")

    def test_cmp(self):
        self.assertTrue(self.p1 == Point(1, 2))
        self.assertTrue(self.p1 != self.p2)

    def test_add(self):
        self.assertEqual(self.p1 + self.p2, Point(-1, 6))
        self.assertEqual(self.p1 + self.p3, Point(4, 7))

    def test_sub(self):
        self.assertEqual(self.p1 - self.p2, Point(3, -2))
        self.assertEqual(self.p1 - self.p3, Point(-2, -3))

    def test_mul(self):
        self.assertEqual(self.p1 * self.p2, 6)
        self.assertEqual(self.p1 * self.p3, 13)

    def test_cross(self):
        self.assertEqual(self.p1.cross(self.p2), 8)
        self.assertEqual(self.p1.cross(self.p3), -1)

    def test_length(self):
        self.assertEqual(self.p1.length(), math.sqrt(5))
        self.assertEqual(self.p2.length(), math.sqrt(20))

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()