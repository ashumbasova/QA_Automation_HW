import math

class Square:

    def __init__(self, side1 = 0, side2 = 0):
        self.side1 = side1
        self.side2 = side2

    def __str__(self):
        return "side1: {}, side2: {}".format(self.side1, self.side2)

    def S(self, S):
        return self.side1 * self.side2

    def P(self, P):
        return self.side1 + self.side1 + self.side2 + self.side2


class XY:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


    def distance(self):
        return math.sqrt(math.pow((self.x), 2) + math.pow((self.y), 2))

    def minus(self, p2):
        return math.sqrt(math.pow((self.x - p2.x), 2) + math.pow((self.y - p2.y), 2))

    def rad(self):
        return (math.sqrt(self.x**2 + self.y**2), math.degrees(math.atan(self.y/self.x)))