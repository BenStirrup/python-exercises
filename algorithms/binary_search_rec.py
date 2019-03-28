def binary_search_rec(items, item):
    """ Recursive implementation
    Assumptions: items is a list of ordered integers
    """
    if not items:
        return False

    if len(items) == 1:
        if items[0] == item:
            return True
        return False

    middle_index = int(len(items) / 2)
    middle_item = items[middle_index]

    if middle_item > item:
        return binary_search_rec(items[:middle_index], item)
    elif middle_item < item:
        return binary_search_rec(items[middle_index:], item)

    return True
