from algorithms.utils import swap


def bubble_sort(items):
    """ 
    Assumptions: items is a list of integers
    """
    are_items_sorted = False
    i = 0
    while not are_items_sorted:
        # flag to avoid doing unecessary loops when items are sorted
        are_items_sorted = True
        for j in range(0, len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = swap(items[j], items[j + 1])
                are_items_sorted = False
        i += 1
    return items
