def change_making(denominations, amount):
    """Returns the minimum number of coins needed to make change for amount.
    denominations is a list of coin denominations, e.g. [1, 5, 10, 25]
    amount is the amount of change to make
    """
    if amount == 0:
        return 0

    min_coins = amount
    for coin in denominations:
        if coin <= amount:
            num_coins = 1 + change_making(denominations, amount - coin)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins


def change_making_dp(denominations, amount):
    """Returns the minimum number of coins needed to make change for amount.
    denominations is a list of coin denominations, e.g. [1, 5, 10, 25]
    amount is the amount of change to make
    """
    min_coins = [0 for _ in range(amount + 1)]
    for cents in range(amount + 1):
        coin_count = cents
        for d in denominations:
            if d <= cents:
                if min_coins[cents - d] + 1 < coin_count:
                    coin_count = min_coins[cents - d] + 1
        min_coins[cents] = coin_count

    return min_coins[amount]


if __name__ == "__main__":
    denominations = [1, 5, 10, 25, 50]
    amount = 63

    print(
        "Minimum number of coins to make change for {} using {} is {}".format(
            amount, denominations, change_making_dp(denominations, amount)
        )
    )
