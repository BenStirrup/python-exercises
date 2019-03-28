def binary_search_iter(items, item):
    """ Iterative implementation
    Assumptions: items is a list of ordered integers
    """
    if not items:
        return False

    while items:
        if len(items) == 1:
            if items[0] == item:
                return True
            return False

        middle_index = int(len(items) / 2)
        middle_item = items[middle_index]
        if middle_item > item:
            items = items[:middle_index]
        elif middle_item < item:
            items = items[middle_index:]
        else:
            return True
