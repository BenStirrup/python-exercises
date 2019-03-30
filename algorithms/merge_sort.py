def merge_sort(items):
    """ 
    Assumptions: items is a list of integers
    """
    if len(items) <= 1:
        return items

    middle_index = int(len(items) / 2)

    left = items[:middle_index]
    right = items[middle_index:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    sorted_items = []
    i, j = 0, 0
    while i < len(sorted_left) and j < len(sorted_right):
        if sorted_left[i] < sorted_right[j]:
            sorted_items.append(sorted_left[i])
            i += 1
        else:
            sorted_items.append(sorted_right[j])
            j += 1

    while i < len(sorted_left):
        sorted_items.append(sorted_left[i])
        i += 1

    while j < len(sorted_right):
        sorted_items.append(sorted_right[j])
        j += 1

    return sorted_items


if __name__ == "__main__":
    merge_sort([5, 6, 7, 2, 2, 4, 5, 8])