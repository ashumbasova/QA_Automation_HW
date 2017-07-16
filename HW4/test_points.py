import unittest
from Points import XY

class DistanceTests(unittest.TestCase):
    def test_one(self):
        p1 = XY(3, 4)
        self.assertEqual(p1.distance(), 5)

class MinusTests(unittest.TestCase):
    def test_two(self):
        p1 = XY(1,1)
        p2 = XY(2,1)

        self.assertEqual(p1.minus(p2), 1)

class RadTests(unittest.TestCase):
    def test_three(self):
        p1 = XY(1, 1)
        self.assertEqual(p1.rad(), (2**0.5, 45))