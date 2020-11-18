from statzcw import zstderr
from scipy.stats import sem
import unittest


class TestZStderr(unittest.TestCase):

    def test_stderr1(self):
        test_data = [1, 2, 3, 4, 5]
        self.assertEqual(round(sem(test_data), 5), zstderr.stderr(test_data))

    def test_stderr2(self):
        test_data = [6, 7, 8, 9, 10]
        self.assertEqual(round(sem(test_data), 5), zstderr.stderr(test_data))

    def test_stderr3(self):
        test_data = [-10, -20, -30, -40, -50]
        self.assertEqual(round(sem(test_data), 5), zstderr.stderr(test_data))


if __name__ == '__main__':
    unittest.main()
