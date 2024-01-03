import unittest
from fracs import *
class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero1 = [0, 1]
        self.zero2 = [0, 4]

        self.frac1 = [1, 8]
        self.frac2 = [7, 4]
        self.frac3 = [-1, 3]
        self.frac4 = [3, -2]
        self.frac5 = [-3, -4]
        self.frac6 = [-5, -3]

    def test_add_frac(self):
        self.assertEqual(add_frac(self.frac1, self.frac2), [15, 8])
        self.assertEqual(add_frac(self.frac1, self.frac3), [-5, 24])
        self.assertEqual(add_frac(self.frac5, self.frac6), [29, 12])

    def test_sub_frac(self):
        self.assertEqual(sub_frac(self.frac1, self.frac2), [-13, 8])
        self.assertEqual(sub_frac(self.frac1, self.frac3), [11, 24])
        self.assertEqual(sub_frac(self.frac5, self.frac6), [-11, 12])

    def test_mul_frac(self):
        self.assertEqual(mul_frac(self.frac1, self.frac2), [7, 32])
        self.assertEqual(mul_frac(self.frac1, self.frac3), [-1, 24])
        self.assertEqual(mul_frac(self.frac5, self.frac6), [5, 4])

    def test_div_frac(self):
        self.assertEqual(div_frac(self.frac1, self.frac2), [1, 14])
        self.assertEqual(div_frac(self.frac1, self.frac3), [3, -8])
        self.assertEqual(div_frac(self.frac5, self.frac6), [9, 20])

    def test_is_positive(self):
        self.assertFalse(is_positive(self.zero1))
        self.assertFalse(is_positive(self.frac3))
        self.assertFalse(is_positive(self.frac4))

        self.assertTrue(is_positive(self.frac1))
        self.assertTrue(is_positive(self.frac5))

    def test_is_zero(self):
        self.assertTrue(is_zero(self.zero1))
        self.assertTrue(is_zero(self.zero2))
        self.assertFalse(is_zero(self.frac2))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac(self.frac1, self.frac2), 1)
        self.assertEqual(cmp_frac(self.frac1, self.frac3), -1)
        self.assertEqual(cmp_frac(self.zero1, self.zero2), 0)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)

    def test_frac2float(self):
        self.assertEqual(frac2float(self.frac1), 0.125)
        self.assertEqual(frac2float(self.zero2), 0.0)
        self.assertEqual(frac2float(self.frac5), 0.75)

    def test_is_valid(self):
        self.assertIsNone(is_valid([1, 2]))
        self.assertIsNone(is_valid([1, 2]))
        self.assertIsNone(is_valid([-5, 2]))
        self.assertIsNone(is_valid([-5, 2], [3, 2], [4, 2]))

        with self.assertRaises(ValueError):
            is_valid([1, 2, 3])
        with self.assertRaises(ValueError):
            is_valid([1])
        with self.assertRaises(ValueError):
            is_valid([])

        with self.assertRaises(ValueError):
            is_valid([1, 0])

        with self.assertRaises(ValueError):
            is_valid([1.5, 2])
        with self.assertRaises(ValueError):
            is_valid([1, 1.3])


    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy