# def is_single_riffle(half1, half2, shuffled_deck):
#     """Recursive implementation: O(n) time, O(n) space"""

#     if not shuffled_deck:
#         if not half1 and not half2:
#             return True
#         return False

#     first_card_shuffled_deck = shuffled_deck.pop()

#     if half1 and first_card_shuffled_deck == half1[-1]:
#         half1.pop()
#         return is_single_riffle(half1, half2, shuffled_deck)

#     if half2 and first_card_shuffled_deck == half2[-1]:
#         half2.pop()
#         return is_single_riffle(half1, half2, shuffled_deck)

#     return False


def is_single_riffle(half1, half2, shuffled_deck):
    """Iterative implementation: O(n) time, O(1) space"""

    while shuffled_deck:
        first_card_shuffled_deck = shuffled_deck.pop()

        if half1 and first_card_shuffled_deck == half1[-1]:
            half1.pop()
        elif half2 and first_card_shuffled_deck == half2[-1]:
            half2.pop()
        else:
            return False

        if not half1 and not half2:
            return True

    return False


if __name__ == "__main__":
    result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
    print(result)
