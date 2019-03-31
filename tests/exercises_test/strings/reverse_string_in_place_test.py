import unittest

from exercises.strings.reverse_string_in_place import reverse_string_in_place


class Test(unittest.TestCase):
    def test_empty_string(self):
        list_of_chars = []
        reverse_string_in_place(list_of_chars)
        expected = []
        self.assertEqual(list_of_chars, expected)

    def test_single_character_string(self):
        list_of_chars = ["A"]
        reverse_string_in_place(list_of_chars)
        expected = ["A"]
        self.assertEqual(list_of_chars, expected)

    def test_longer_string(self):
        list_of_chars = ["A", "B", "C", "D", "E"]
        reverse_string_in_place(list_of_chars)
        expected = ["E", "D", "C", "B", "A"]
        self.assertEqual(list_of_chars, expected)
