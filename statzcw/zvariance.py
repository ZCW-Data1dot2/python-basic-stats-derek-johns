from statzcw import zmean, zcount


def variance(in_list):
    """
    Finds variance of given list
    :param in_list: list of values
    :return: float rounded to 5 decimal places
    """
    n = zcount.count(in_list)
    mean = zmean.mean(in_list)
    d = [(x - mean) ** 2 for x in in_list]
    v = sum(d) / (n - 1)
    return round(v, 5)