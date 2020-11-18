from statzcw import zstddev, zcount
from math import sqrt


def stderr(in_list):
    """
    Calculates standard error of mean of given list
    :param in_list: list of values
    :return: float rounded to 5 decimal places
    """
    std_dev = zstddev.stddev(in_list)
    n = zcount.count(in_list)
    std_err = std_dev / sqrt(n)
    return round(std_err, 5)
