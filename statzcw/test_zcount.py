from statzcw import zcount
import unittest


class TestZCount(unittest.TestCase):

    def test_count1(self):
        test_data = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(len(test_data), zcount.count(test_data))

    def test_count2(self):
        test_data = []
        self.assertEqual(len(test_data), zcount.count(test_data))

    def test_count3(self):
        test_data = [1, 1, 1]
        self.assertEqual(len(test_data), zcount.count(test_data))


if __name__ == '__main__':
    unittest.main()
