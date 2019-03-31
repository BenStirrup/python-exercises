def reverse_string_in_place(list_of_chars: list):
    if not list_of_chars:
        return []

    n = len(list_of_chars)
    i, j = 0, n - 1
    while i < j:
        list_of_chars[i], list_of_chars[j] = list_of_chars[j], list_of_chars[i]
        i = i + 1
        j = j - 1

    return list_of_chars


if __name__ == "__main__":
    reversed_list_of_chars = reverse_string_in_place(["A", "B", "C", "D", "E", "F"])
    print(reversed_list_of_chars)
