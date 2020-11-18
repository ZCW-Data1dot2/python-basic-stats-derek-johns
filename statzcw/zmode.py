from collections import Counter


def mode(in_list):
    """
    Finds mode of given list
    :param in_list: list of values
    :return: int, float, None if no mode, or list if multiple modes
    """
    c = Counter(in_list)
    if max(c.values()) == 1:
        return None
    else:
        return max(c, key=c.get)
