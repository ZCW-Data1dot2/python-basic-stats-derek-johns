from statzcw import csvReader
import unittest
import csv
from os import remove


class TestCsvReader(unittest.TestCase):

    def test_read_csv(self):

        test_file = 'test_file.csv'

        test_data = [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]
            ]

        with open(test_file, 'w') as f:
            field_names = ('x', 'y')
            writer = csv.writer(f)
            writer.writerow(field_names)
            for i in tuple(zip(test_data[0], test_data[1])):
                writer.writerow(i)

        self.assertEqual(test_data, csvReader.read_csv(test_file))
        remove(test_file)

    def test_read_csv2(self):

        test_file = 'test_file.csv'

        test_data = [
            [-10, -20, -30, -40, -50],
            [-60, -70, -80, -90, -100]
        ]

        with open(test_file, 'w') as f:
            field_names = ('x', 'y')
            writer = csv.writer(f)
            writer.writerow(field_names)
            for i in tuple(zip(test_data[0], test_data[1])):
                writer.writerow(i)

        self.assertEqual(test_data, csvReader.read_csv(test_file))
        remove(test_file)


if __name__ == '__main__':
    unittest.main()
