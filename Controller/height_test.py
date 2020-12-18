import unittest

from Model.data import SPHEROMETR
from Controller.calculator import concave_height


class TestConcaveHeight(unittest.TestCase):

    def test_concave_100(self):
        type = SPHEROMETR["BIG"]
        ring = SPHEROMETR["RING_1"]
        self.assertEqual(concave_height(1000, type, ring), 1.590, "It the test")


if __name__ == '__main__':
    unittest.main()
