# Calculate the max profit
def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        return None

    lowest_price = stock_prices[0]
    max_benefit = stock_prices[1] - lowest_price

    for price in stock_prices[1:]:
        benefit = price - lowest_price

        max_benefit = max(benefit, max_benefit)
        lowest_price = min(price, lowest_price)

    return max_benefit


# Tests
import unittest


class Test(unittest.TestCase):
    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        self.assertEqual(get_max_profit([]), None)

    def test_error_with_one_price(self):
        self.assertEqual(get_max_profit([1]), None)


unittest.main(verbosity=2)
