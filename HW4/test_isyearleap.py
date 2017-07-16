import unittest
from IsYearLeap import isYearLeap

class LeapTests(unittest.TestCase):
    def test_zero(self):
        res = isYearLeap(40)
        self.assertEqual(res, True)

    def test_one(self):
        res = isYearLeap(400)
        self.assertEqual(res, True)
    def test_two(self):
        res = isYearLeap(2017)
        self.assertEqual(res, False)