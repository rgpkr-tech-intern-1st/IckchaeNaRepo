import find_number as fn
import unittest
import sys


class TestFindNumber(unittest.TestCase):
    def setUp(self):
        self.low_int = -sys.maxint
        self.high_int = sys.maxint
        self.n = 1954421783993232787

    def tearDown(self):
        print("Success")

    def test_find_number(self):
        guess_num = fn.binary_search(self.low_int, self.high_int)
        self.assertEqual(self.n, guess_num)


if __name__ == '__main__':
    unittest.main()
