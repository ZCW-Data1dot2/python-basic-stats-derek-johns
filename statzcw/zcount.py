def count(in_list):
    """
    Returns the number of elements in the list
    :param in_list: list of elements
    :return: int representing number of elements in given list
    """
    c = 0
    for _ in in_list:
        c += 1
    return c
