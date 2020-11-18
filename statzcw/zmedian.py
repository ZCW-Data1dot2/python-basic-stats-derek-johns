def median(in_list):
    """
    Finds median value of given list
    :param in_list: list of values
    :return: float or int
    """
    n = len(in_list)
    in_list.sort()
    if n % 2 == 0:
        m1 = in_list[n // 2]
        m2 = in_list[n // 2 - 1]
        m = (m1 + m2) / 2
    else:
        m = in_list[n // 2]
    return m
