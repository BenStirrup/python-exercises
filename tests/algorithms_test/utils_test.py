import unittest

from algorithms.utils import swap


class Test(unittest.TestCase):

    def test_swap_two_items(self):
        item1, item2 = 1, 2
        item1, item2 = swap(item1, item2)
        self.assertEqual(item1, 2)
        self.assertEqual(item2, 1)
