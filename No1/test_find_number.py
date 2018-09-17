import find_number as fn
import unittest
import sys


class TestFindNumber(unittest.TestCase):
    def setUp(self):
        self.low_int = -sys.maxint
        self.high_int = sys.maxint
        self.n = 0

    def tearDown(self):
        self.low_int = None
        self.high_int = None
        self.n = None

    def test_find_number(self):
        self.n = 1954421783993232787
        guess_num = fn.binary_search(self.low_int, self.high_int)
        self.assertEqual(self.n, guess_num)

    def test_find_even_num(self):
        self.n = 100
        guess_num = fn.binary_search_little_num(self.low_int, self.high_int, self.n)
        self.assertEqual(self.n, guess_num)

    def test_find_odd_num(self):
        self.n = 55
        guess_num = fn.binary_search_little_num(self.low_int, self.high_int, self.n)
        self.assertEqual(self.n, guess_num)


if __name__ == '__main__':
    unittest.main()
