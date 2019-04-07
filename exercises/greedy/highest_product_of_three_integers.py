def highest_product_of_3(integers):
    if len(integers) < 3:
        raise ValueError("Integer list must have at least 3 integers")

    highest = max(integers[0], integers[1])
    lowest = min(integers[0], integers[1])
    highest_product_of_2 = integers[0] * integers[1]
    lowest_product_of_2 = integers[0] * integers[1]
    highest_product_of_3 = integers[0] * integers[1] * integers[2]

    for integer in integers[2:]:
        highest_product_of_3 = max(
            highest_product_of_3,
            integer * highest_product_of_2,
            integer * lowest_product_of_2,
        )

        highest_product_of_2 = max(
            highest_product_of_2, integer * highest, integer * lowest
        )

        lowest_product_of_2 = min(
            lowest_product_of_2, integer * highest, integer * lowest
        )

        highest = max(highest, integer)
        lowest = min(lowest, integer)

    return highest_product_of_3
