import unittest

from exercises.hash_table.word_cloud import word_cloud


class Test(unittest.TestCase):
    def test_simple_sentence(self):
        input = "I like cake"
        actual = word_cloud(input)
        expected = {"I": 1, "like": 1, "cake": 1}
        self.assertEqual(actual, expected)

    def test_longer_sentence(self):
        input = "Chocolate cake for dinner and pound cake for dessert"
        actual = word_cloud(input)
        expected = {
            "and": 1,
            "pound": 1,
            "for": 2,
            "dessert": 1,
            "Chocolate": 1,
            "dinner": 1,
            "cake": 2,
        }
        self.assertEqual(actual, expected)

    def test_punctuation(self):
        input = "Strawberry short cake? Yum!"
        actual = word_cloud(input)
        expected = {"cake": 1, "Strawberry": 1, "short": 1, "Yum": 1}
        self.assertEqual(actual, expected)

    def test_hyphenated_words(self):
        input = "Dessert - mille-feuille cake"
        actual = word_cloud(input)
        expected = {"cake": 1, "Dessert": 1, "mille-feuille": 1}
        self.assertEqual(actual, expected)

    def test_ellipses_between_words(self):
        input = "Mmm...mmm...decisions...decisions"
        actual = word_cloud(input)
        expected = {"mmm": 2, "decisions": 2}
        self.assertEqual(actual, expected)

    def test_apostrophes(self):
        input = "Allie's Bakery: Sasha's Cakes"
        actual = word_cloud(input)
        expected = {"Bakery": 1, "Cakes": 1, "Allie's": 1, "Sasha's": 1}
        self.assertEqual(actual, expected)
