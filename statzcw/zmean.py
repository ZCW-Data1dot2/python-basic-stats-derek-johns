from statzcw import zcount


def mean(in_list):
    """
    Returns mean of given list
    :param in_list: list to calculate mean from
    :return: float rounded to 5 decimal places
    """
    return round(sum(in_list) / zcount.count(in_list), 5)
