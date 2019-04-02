def merge_ordered_lists(list1, list2):
    if not list1 and not list2:
        return []

    if not list1:
        return list2

    if not list2:
        return list1

    merged_list = []
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i = i + 1
        else:
            merged_list.append(list2[j])
            j = j + 1
    
    while i < len(list1):
        merged_list.append(list1[i])
        i = i + 1

    while j < len(list2):
        merged_list.append(list2[j])
        j = j + 1

    return merged_list

if __name__ == "__main__":
    merged_list = merge_ordered_lists([2, 4, 6, 8], [1, 7])
    print("Merged list: ", merged_list)
