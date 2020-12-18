import unittest

from Model.data import SPHEROMETR
from Controller.calculator import concave_height, convex_height


class TestConcaveHeight(unittest.TestCase):

    def test_concave_1000_big_1(self):
        type = "BIG"
        ring ="RING_1"
        self.assertEqual(
            concave_height(1000, type, ring), 1.018, "Стрелка должна быть 1,018мм")

    def test_concave_500_big_2(self):
        type = "BIG"
        ring ="RING_2"
        self.assertEqual(
            concave_height(500, type, ring), 5.688, "Стрелка должна быть 5,688мм")


class TestConvexHeight(unittest.TestCase):

    def test_convex_1000_big_1(self):
        type = "BIG"
        ring ="RING_1"
        self.assertEqual(
            convex_height(1000, type, ring), 1.012, "Стрелка должна быть 1,012мм")


    def test_convex_500_big_2(self):
        type = "BIG"
        ring ="RING_2"
        self.assertEqual(
            convex_height(500, type, ring), 5.616, "Стрелка должна быть 5,616мм")


if __name__ == '__main__':
    unittest.main()
