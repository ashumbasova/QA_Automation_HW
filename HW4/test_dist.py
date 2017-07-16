import unittest
from Distance import distance

class DistanceTests (unittest.TestCase):
    def test_zero(self):
        res = distance(0, 0, 0, 0)
        self.assertEqual(res, 0)

    def test_one(self):
        res = distance(0, 0, 0, 1)
        self.assertEqual(res, 1)

    def test_two(self):
        res = distance(0, 0, 1, 1)
        self.assertEqual(res, 2**0.5)

    def test_three(self):
        res = distance(1, 1, 1, 1)
        self.assertEqual(res, 0)

    def test_four(self):
        res = distance(-1, 1, 1, -1)
        self.assertEqual(res, 8**0.5)