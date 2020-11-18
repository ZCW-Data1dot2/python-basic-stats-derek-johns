from statzcw import zcount
from math import sqrt


def corr(l1, l2):
    """
    Calculates the correlation between two lists of values
    :param l1: list of values
    :param l2: list of values
    :return: float rounded to 5 decimal places
    """
    l1_sum = sum(l1)
    l2_sum = sum(l2)
    l1_times_l2_sum = sum([l1[i] * l2[i] for i in range(len(l1))])
    l1_sq_sum = sum([x ** 2 for x in l1])
    l2_sq_sum = sum([x ** 2 for x in l2])
    n = zcount.count(l1)
    corr_num = (n * l1_times_l2_sum) - (l1_sum * l2_sum)
    corr_den = sqrt(((n * l1_sq_sum) - (l1_sum ** 2)) * ((n * l2_sq_sum) - (l2_sum ** 2)))
    corr = corr_num / corr_den
    return round(corr, 5)