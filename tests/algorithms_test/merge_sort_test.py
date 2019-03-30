import unittest

from algorithms.merge_sort import merge_sort

class Test(unittest.TestCase):
    def test_no_items(self):
        actual = merge_sort([])
        self.assertEqual(actual, [])

    def test_five_unsorted_items(self):
        actual = merge_sort([3, 5, 1, 6, 4])
        self.assertEqual(actual, [1, 3, 4, 5, 6])

    def test_five_sorted_items(self):
        actual = merge_sort([1, 3, 4, 5, 6])
        self.assertEqual(actual, [1, 3, 4, 5, 6])

    def test_five_inversely_sorted_items(self):
        actual = merge_sort([5, 4, 3, 2, 1])
        self.assertEqual(actual, [1, 2, 3, 4, 5])