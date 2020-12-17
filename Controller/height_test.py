import unittest

class TestHeight(unittest.TestCase):

    def test_concave_100(self):
        self.assertEqual(50 + 50, 100, "Should be 100")

if __name__ == '__main__':
    unittest.main()
