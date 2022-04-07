# TEST

import unittest
from circle import getArea, getPerimetr

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(10), 314.159)
        self.assertAlmostEqual(getArea(3), 28.27431)
    def test_perimetr(self):
        self.assertAlmostEqual(getPerimetr(10), 62.8318)
        self.assertAlmostEqual(getPerimetr(4), 25.13272)
        
unittest.main()
        
        
        