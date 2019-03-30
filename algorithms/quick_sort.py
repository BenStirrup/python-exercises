def quick_sort(items):
    """ 
    Assumptions: items is a list of integers
    """
    n = len(items)
    if n <= 1:
        return items

    pivot = items[0]
    leftmark = items[1]
    rightmark = items[n-1]

    done = False
    left_array, right_array = [], []
    leftmark, rightmark = 1, n - 1
    while not done:
        while leftmark <= rightmark and items[leftmark] <= pivot:
            left_array.append(items[leftmark])
            leftmark += 1

        while leftmark <= rightmark and items[rightmark] >= pivot:
            right_array.append(items[rightmark])
            rightmark -= 1

        if leftmark > rightmark:
            done = True
        else:
            items[leftmark], items[rightmark] = items[rightmark], items[leftmark]
        
    return quick_sort(left_array) + [pivot] + quick_sort(right_array)


if __name__ == "__main__":
    sorted_items = quick_sort([5, 6, 7, 4, 8])
    print(sorted_items)