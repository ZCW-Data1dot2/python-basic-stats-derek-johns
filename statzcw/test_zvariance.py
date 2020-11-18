from statzcw import zvariance
from statistics import variance
import unittest


class TestZVariance(unittest.TestCase):

    def test_variance1(self):
        test_data = [1, 2, 3, 4, 5]
        self.assertEqual(round(variance(test_data), 5), zvariance.variance(test_data))

    def test_stddev2(self):
        test_data = [6, 7, 8, 9, 10]
        self.assertEqual(round(variance(test_data), 5), zvariance.variance(test_data))

    def test_stddev3(self):
        test_data = [-10, -20, -30, -40, -50]
        self.assertEqual(round(variance(test_data), 5), zvariance.variance(test_data))


if __name__ == '__main__':
    unittest.main()
