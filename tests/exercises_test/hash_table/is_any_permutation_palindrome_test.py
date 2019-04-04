import unittest

from exercises.hash_table.is_any_permutation_palindrome import (
    is_any_permutation_palindrome,
)


class Test(unittest.TestCase):
    def test_permutation_with_odd_number_of_chars(self):
        result = is_any_permutation_palindrome("aabcbcd")
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = is_any_permutation_palindrome("aabccbdd")
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = is_any_permutation_palindrome("aabcd")
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = is_any_permutation_palindrome("aabbcd")
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_any_permutation_palindrome("")
        self.assertTrue(result)

    def test_one_character_string(self):
        result = is_any_permutation_palindrome("a")
        self.assertTrue(result)
