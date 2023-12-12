class Item:
    def __init__(self, weight, value) -> None:
        self.weight = weight
        self.value = value


class Knapsack:
    def __init__(self, items, max_weight) -> None:
        memory = [[-1 for _ in range(max_weight + 1)] for _ in range(len(items) + 1)]
        for i in range(len(items) + 1):
            memory[i][0] = 0
        for j in range(max_weight + 1):
            memory[0][j] = 0

        self.memory = memory
        self.items = items
        self.max_weight = max_weight

    def solve(self):
        return self.__solve(len(self.items), self.max_weight)

    def __solve(self, i, j):
        if self.memory[i][j] < 0:
            if j < self.items[i - 1].weight:
                value = self.__solve(i - 1, j)
            else:
                value = max(
                    self.__solve(i - 1, j),
                    self.__solve(i - 1, j - self.items[i - 1].weight)
                    + self.items[i - 1].value,
                )
            self.memory[i][j] = value

        return self.memory[i][j]


if __name__ == "__main__":
    import random

    items = int(input())
    max_weight = int(input())

    # Generate random integer weights between 1 and 100
    items = [Item(random.randint(1, 100), random.randint(1, 5)) for _ in range(items)]

    # Print the items and the values
    for item in items:
        print("Item: weight={}, value={}".format(item.weight, item.value))

    # Solve the knapsack problem
    knapsack = Knapsack(items, max_weight)

    print(
        "Maximum value for {} items with maximum weight of {} is {}".format(
            len(items), max_weight, knapsack.solve()
        )
    )
