import unittest

from algorithms.quick_sort import quick_sort


class Test(unittest.TestCase):
    def test_no_items(self):
        actual = quick_sort([])
        self.assertEqual(actual, [])

    def test_five_unsorted_items(self):
        actual = quick_sort([3, 5, 1, 6, 4])
        self.assertEqual(actual, [1, 3, 4, 5, 6])

    def test_five_sorted_items(self):
        actual = quick_sort([1, 3, 4, 5, 6])
        self.assertEqual(actual, [1, 3, 4, 5, 6])

    def test_fifteen_unsorted_tems(self):
        actual = quick_sort([16, 15, 29, 4, 23, 8, 10, 28, 25, 19, 27, 24, 7, 30, 5])
        self.assertEqual(actual, [4, 5, 7, 8, 10, 15, 16, 19, 23, 24, 25, 27, 28, 29, 30])

    def test_five_inversely_sorted_items(self):
        actual = quick_sort([5, 4, 3, 2, 1])
        self.assertEqual(actual, [1, 2, 3, 4, 5])

