from statzcw import zcorr
from scipy.stats import pearsonr
import unittest


class TestZCorr(unittest.TestCase):

    def test_corr1(self):
        td1 = [1, 2, 3, 4, 5]
        td2 = [1, 2, 3, 4, 5]
        self.assertEqual(round(pearsonr(td1, td2)[0], 5), zcorr.corr(td1, td2))

    def test_corr2(self):
        td1 = [6, 7, 8, 9, 10]
        td2 = [1, 2, 3, 4, 5]
        self.assertEqual(round(pearsonr(td1, td2)[0], 5), zcorr.corr(td1, td2))

    def test_corr3(self):
        td1 = [-10, -20, -30, -40, -50]
        td2 = [1, 2, 3, 4, 5]
        self.assertEqual(round(pearsonr(td1, td2)[0], 5), zcorr.corr(td1, td2))


if __name__ == '__main__':
    unittest.main()

