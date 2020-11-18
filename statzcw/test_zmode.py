from statzcw import zmode
from statistics import mode
import unittest


class TestZMode(unittest.TestCase):

    def test_mode1(self):
        test_data = [1, 2, 3, 4, 5, 5]
        self.assertEqual(mode(test_data), zmode.mode(test_data))

    def test_mode2(self):
        test_data = [1, 2, 3, 4, 5, 2, 3, 2]
        self.assertEqual(mode(test_data), zmode.mode(test_data))

    def test_mode3(self):
        test_data = [1, 2, 3, 4, 5, 3, 3]
        print(zmode.mode(test_data))
        self.assertEqual(mode(test_data), zmode.mode(test_data))


if __name__ == '__main__':
    unittest.main()
