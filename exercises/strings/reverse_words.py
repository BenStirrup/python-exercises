def reverse_string_in_place(list_of_chars: list, start, end):
    if not list_of_chars:
        return []

    while start < end:
        list_of_chars[start], list_of_chars[end] = (
            list_of_chars[end],
            list_of_chars[start],
        )
        start = start + 1
        end = end - 1


def reverse_words(list_of_chars: list):
    if not list_of_chars:
        return [""]

    n = len(list_of_chars)
    reverse_string_in_place(list_of_chars, 0, n - 1)

    current_word_start = 0
    for idx in range(0, n):
        char = list_of_chars[idx]

        if char == " ":
            reverse_string_in_place(list_of_chars, current_word_start, idx - 1)
            current_word_start = idx + 1

        if idx == n - 1:
            reverse_string_in_place(list_of_chars, current_word_start, idx)


if __name__ == "__main__":
    sentence = ["B", "E", "N", " ", "T", "H", "U", "G", " ", "L", "O", "L"]
    reverse_words(sentence)
    print(sentence)
    print(reverse_words(list("thief cake")))

