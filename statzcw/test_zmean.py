from statzcw import zmean
from statistics import mean
import unittest


class TestZMean(unittest.TestCase):

    def test_mean1(self):
        test_data = [1, 2, 3, 4, 5]
        self.assertEqual(mean(test_data), zmean.mean(test_data))

    def test_mean2(self):
        test_data = [-1, -2, -3, -4, -5]
        self.assertEqual(mean(test_data), zmean.mean(test_data))

    def test_mean3(self):
        test_data = [5, 5, 5, 5]
        self.assertEqual(mean(test_data), zmean.mean(test_data))


if __name__ == '__main__':
    unittest.main()
