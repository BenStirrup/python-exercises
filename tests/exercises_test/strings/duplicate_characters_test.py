import unittest

from exercises.strings.duplicate_characters import find_duplicates

class TestFindDuplicates(unittest.TestCase):
    def test_one_duplicated_char(self):
        self.assertEqual(find_duplicates("Java"), "a")

    def test_two_duplicated_chars(self):
        self.assertEqual(find_duplicates("coco"), "c,o")

    def test_two_tripled_chars(self):
        self.assertEqual(find_duplicates("cococo"), "c,o")

    def test_no_duplicate(self):
        self.assertEqual(find_duplicates("ben"), None)

    def test_falsy_input_values(self):
        self.assertEqual(find_duplicates(None), None)
        self.assertEqual(find_duplicates(""), None)
