import enum
import random


def random_coins(n, real, fake):
    assert n > 0
    coins = [real] * (n - 1) + [fake] * (1)
    random.shuffle(coins)
    return coins


Scale = enum.Enum("Scale", ["LeftHeavy", "RightHeavy", "Balanced"])


def compare(left, right) -> Scale:
    delta = sum(right) - sum(left)
    if delta < 0:
        return Scale.LeftHeavy
    elif delta > 0:
        return Scale.RightHeavy
    else:
        return Scale.Balanced


def find_fake_coin(coins):
    if len(coins) == 1:
        return coins[0]

    mid = len(coins) // 2
    left = coins[:mid]
    right = coins[mid : 2 * mid]

    result = compare(left, right)

    print("{} - {}".format(left, right))
    if result == Scale.LeftHeavy:
        return find_fake_coin(right)
    elif result == Scale.RightHeavy:
        return find_fake_coin(left)
    elif result == Scale.Balanced:
        return find_fake_coin(coins[2 * mid :])


if __name__ == "__main__":
    coins = random_coins(10, 1, 0)

    print(coins)

    print(find_fake_coin(coins))
