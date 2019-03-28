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
