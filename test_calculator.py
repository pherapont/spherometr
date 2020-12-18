import unittest

from Model.data import SPHEROMETR
from Controller.calculator import concave_height, convex_height
from Controller.calculator import concave_radius, convex_radius


class TestConcaveHeight(unittest.TestCase):

    def test_concave_1000_big_1(self):
        kind = "BIG"
        ring ="RING_1"
        self.assertEqual(
            concave_height(1000, kind, ring), 1.018, "Стрелка должна быть 1,018мм")

    def test_concave_500_big_2(self):
        kind = "BIG"
        ring ="RING_2"
        self.assertEqual(
            concave_height(500, kind, ring), 5.688, "Стрелка должна быть 5,688мм")

    def test_concave_755_big_3(self):
        kind = "BIG"
        ring ="RING_3"
        self.assertEqual(
            concave_height(755, kind, ring), 8.088, "Стрелка должна быть 8.088мм")

    def test_concave_2000_big_4(self):
        kind = "BIG"
        ring ="RING_4"
        self.assertEqual(
            concave_height(2000, kind, ring), 5.641, "Стрелка должна быть 5,641мм")


class TestConvexHeight(unittest.TestCase):

    def test_convex_1000_big_1(self):
        kind = "BIG"
        ring ="RING_1"
        self.assertEqual(
            convex_height(1000, kind, ring), 1.012, "Стрелка должна быть 1,012мм")


    def test_convex_500_big_2(self):
        kind = "BIG"
        ring ="RING_2"
        self.assertEqual(
            convex_height(500, kind, ring), 5.616, "Стрелка должна быть 5,616мм")

    def test_convex_755_big_3(self):
        kind = "BIG"
        ring ="RING_3"
        self.assertEqual(
            convex_height(755, kind, ring), 8.020, "Стрелка должна быть 8.020мм")

    def test_convex_2000_big_4(self):
        kind = "BIG"
        ring ="RING_4"
        self.assertEqual(
            convex_height(2000, kind, ring), 5.623, "Стрелка должна быть 5.623мм")


class TestConcaveRadius(unittest.TestCase):

    def test_concave_3_033_big_1(self):
        kind = "BIG"
        ring = "RING_1"
        self.assertEqual(
            concave_radius(3.033, kind, ring), 339.2, "Радиус должен быть 339,2мм")

    def test_concave_3_033_big_2(self):
        kind = "BIG"
        ring = "RING_2"
        self.assertEqual(
            concave_radius(3.033, kind, ring), 931.2, "Радиус должен быть 931,2мм")

    def test_concave_3_033_big_3(self):
        kind = "BIG"
        ring = "RING_3"
        self.assertEqual(
            concave_radius(3.033, kind, ring), 1998.8, "Радиус должен быть 1998.8мм")

    def test_concave_3_033_big_4(self):
        kind = "BIG"
        ring = "RING_4"
        self.assertEqual(
            concave_radius(3.033, kind, ring), 3713, "Радиус должен быть 3713мм")


class TestConvexRadius(unittest.TestCase):

    def test_convex_3_033_big_1(self):
        kind = "BIG"
        ring = "RING_1"
        self.assertEqual(
            convex_radius(3.033, kind, ring), 332.9, "Радиус должен быть 332,9мм")

    def test_convex_3_033_big_2(self):
        kind = "BIG"
        ring = "RING_2"
        self.assertEqual(
            convex_radius(3.033, kind, ring), 924.8, "Радиус должен быть 924,8мм")

    def test_convex_3_033_big_3(self):
        kind = "BIG"
        ring = "RING_3"
        self.assertEqual(
            convex_radius(3.033, kind, ring), 1992.5, "Радиус должен быть 1992.5мм")

    def test_convex_3_033_big_4(self):
        kind = "BIG"
        ring = "RING_4"
        self.assertEqual(
            convex_radius(3.033, kind, ring), 3706.7, "Радиус должен быть 3706.7мм")


if __name__ == '__main__':
    unittest.main()
