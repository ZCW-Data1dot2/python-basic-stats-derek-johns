from statzcw import zmedian
from statistics import median
import unittest


class TestZMedian(unittest.TestCase):

    def test_median1(self):
        test_data = [1, 2, 3, 4, 5]
        self.assertEqual(median(test_data), zmedian.median(test_data))

    def test_median2(self):
        test_data = [1, 2, 3, 4, 5, 6]
        self.assertEqual(median(test_data), zmedian.median(test_data))

    def test_median3(self):
        test_data = [1]
        self.assertEqual(median(test_data), zmedian.median(test_data))


if __name__ == '__main__':
    unittest.main()
