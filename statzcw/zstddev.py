from statzcw import zvariance
from math import sqrt


def stddev(in_list):
    """
    Calculates standard deviation of given list
    :param in_list: list of values
    :return: float rounded to 5 decimal places
    """
    var = zvariance.variance(in_list)
    std_dev = sqrt(var)
    return round(std_dev, 5)
