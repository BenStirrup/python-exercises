import unittest


def find_duplicates(string: str):
    if not string:
        return None

    chars = dict()
    duplicated_chars = dict()
    for char in string:
        # Check if char was never seen once
        if not chars.get(char):
            chars[char] = char
        else:
            # Check if char was never seen twice
            if not duplicated_chars.get(char):
                duplicated_chars[char] = char

    if not duplicated_chars:
        return None

    return ",".join(duplicated_chars.keys())


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


if __name__ == "__main__":
    unittest.main()

