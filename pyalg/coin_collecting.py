def coin_collecting(board):
    if len(board) == 0 or len(board[0]) == 0:
        return 0

    return board[0][0] + max(
        coin_collecting(board[1:]), coin_collecting([row[1:] for row in board])
    )


def coin_collecting_dynamic(board):
    n = len(board)
    m = len(board[0])

    memory = [[0 for _ in range(m)] for _ in range(n)]

    memory[0][0] = board[0][0]

    for j in range(1, m):
        memory[0][j] = memory[0][j - 1] + board[0][j]

    for i in range(1, n):
        memory[i][0] = memory[i - 1][0] + board[i][0]
        for j in range(1, m):
            memory[i][j] = max(memory[i - 1][j], memory[i][j - 1]) + board[i][j]

    return memory[-1][-1]


if __name__ == "__main__":
    import random

    n = int(input())
    m = int(input())

    coins_board = [[random.randint(0, 1) for _ in range(m)] for _ in range(n)]

    print("Board:")
    for row in coins_board:
        print(row)

    print("Recursive algorithm: {}".format(coin_collecting(coins_board)))

    print(
        "Dynamic Programming algorithm: {}".format(coin_collecting_dynamic(coins_board))
    )
