import unittest
import math

from circle import Area_Circle, Perimeter_Circle
from Rectangle import Area_Rectangle, Perimeter_Rectangle
from square import Area_square, Perimeter_square

class TestCircle(unittest.TestCase):

    def test_area(self):
        self.assertAlmostEqual(Area_Circle(1), math.pi, places=7)
        self.assertEqual(Area_Circle(0), 0)
        self.assertAlmostEqual(Area_Circle(2), 4 * math.pi, places=7)

    def test_perimeter(self):
        self.assertAlmostEqual(Perimeter_Circle(1), 2 * math.pi, places=7)
        self.assertEqual(Perimeter_Circle(0), 0)
        self.assertAlmostEqual(Perimeter_Circle(2), 4 * math.pi, places=7)


class TestRectangle(unittest.TestCase):

    def test_area_rectangle(self):
        self.assertEqual(Area_Rectangle(2, 3), 6)
        self.assertEqual(Area_Rectangle(0, 5), 0)
        self.assertEqual(Area_Rectangle(4, 4), 16)

    def test_perimeter_rectangle(self):
        self.assertEqual(Perimeter_Rectangle(2, 3), 10)
        self.assertEqual(Perimeter_Rectangle(0, 5), 10)
        self.assertEqual(Perimeter_Rectangle(4, 4), 16)


class TestSquare(unittest.TestCase):

    def test_area_square(self):
        self.assertEqual(Area_square(2), 4)
        self.assertEqual(Area_square(0), 0)
        self.assertEqual(Area_square(5), 25)

    def test_perimeter_square(self):
        self.assertEqual(Perimeter_square(2), 8)
        self.assertEqual(Perimeter_square(0), 0)
        self.assertEqual(Perimeter_square(5), 20)


if __name__ == '__main__':
    unittest.main()