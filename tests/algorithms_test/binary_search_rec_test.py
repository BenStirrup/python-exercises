import unittest

from algorithms.binary_search_rec import binary_search_rec

class Test(unittest.TestCase):
    def test_no_items(self):
        actual = binary_search_rec([], 8)
        self.assertEqual(actual, False)

    def test_one_item_found(self):
        actual = binary_search_rec([6], 6)
        self.assertEqual(actual, True)

    def test_one_item_not_found(self):
        actual = binary_search_rec([6], 4)
        self.assertEqual(actual, False)

    def test_six_items_found(self):
        actual = binary_search_rec([1, 3, 6, 9, 10, 11], 6)
        self.assertEqual(actual, True)

    def test_six_items_not_found(self):
        actual = binary_search_rec([1, 3, 6, 9, 10, 11], 2)
        self.assertEqual(actual, False)

    def test_seven_items_found(self):
        actual = binary_search_rec([1, 3, 6, 9, 10, 11, 15], 3)
        self.assertEqual(actual, True)

    def test_seven_items_not_found(self):
        actual = binary_search_rec([1, 3, 6, 9, 10, 11, 15], 2)
        self.assertEqual(actual, False)
