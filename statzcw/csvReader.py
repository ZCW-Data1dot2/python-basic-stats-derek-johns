import csv


def read_csv(filepath):
    """
    Reads given csv file and returns two lists of x and y values nested within a single list
    :param filepath: str representing csv file
    :return: list of two lists of x and y values
    """
    x = []
    y = []
    with open(filepath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            x.append(float(row['x']))
            y.append(float(row['y']))
    return [x, y]

