def is_any_permutation_palindrome(string):
    """ Check if any permutation of the input is a palindrome:
    1. If each character appears an even number of time
    2. Except for one that can appear an odd number of time, 
     in case the string has an odd length
     """
    odd_chars = set()

    for char in string:
        if char not in odd_chars:
            odd_chars.add(char)
        else:
            odd_chars.remove(char)

    if len(odd_chars) > 1:
        return False

    return True

