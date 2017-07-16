import unittest
from Tringle import triangle

class EquilateralTests(unittest.TestCase):
    def test_one(self):
        res = triangle(3, 3, 3)
        self.assertEqual(res, "Equilateral triangle")

class IsosceleTests(unittest.TestCase):
    def test_two(self):
        res = triangle(3, 3, 5)
        self.assertEqual(res, "Isosceles triangle")

class VersatileTests(unittest.TestCase):
    def test_three(self):
        res = triangle(3, 4, 5)
        self.assertEqual(res, "Versatile triangle")

class NotTriangleTest(unittest.TestCase):
    def test_four(self):
        res = triangle(3, 4, 0)
        self.assertEqual(res, "Not a triangle")