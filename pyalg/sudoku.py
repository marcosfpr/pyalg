class Sudoku:
    def __init__(self, board) -> None:
        self.board = board

    def __str__(self) -> str:
        n = len(self.board)
        assert n % 3 == 0
        s = ""
        for i in range(n):
            if i % 3 == 0:
                s += "-" * (n * 2 + 7) + "\n"
            for j in range(n):
                if j % 3 == 0:
                    s += "| "
                s += str(self.board[i][j]) + " "
            s += "|\n"
        s += "-" * (n * 2 + 7) + "\n"
        return s

    def is_safe(self, row, col, num) -> bool:
        n = len(self.board)
        assert n % 3 == 0

        for i in range(n):
            if self.board[row][i] == num:
                return False

        for i in range(n):
            if self.board[i][col] == num:
                return False

        box_row = row - row % 3
        box_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.board[box_row + i][box_col + j] == num:
                    return False
        return True

    def is_solution(self, row, col) -> bool:
        n = len(self.board)
        return row == n - 1 and col == n

    def is_end_of_row(self, col) -> bool:
        n = len(self.board)
        return col == n

    def solve_backtracing(self, row, col) -> bool:
        n = len(self.board)

        if self.is_solution(row, col):
            return True

        if self.is_end_of_row(col):
            row += 1
            col = 0

        if self.board[row][col] > 0:
            return self.solve_backtracing(row, col + 1)

        for num in range(1, n + 1):
            if self.is_safe(row, col, num):
                self.board[row][col] = num
                if self.solve_backtracing(row, col + 1):
                    return True
            self.board[row][col] = 0
        return False

    def solve(self) -> bool:
        row = col = 0
        if not self.solve_backtracing(row, col):
            return False
        return True


if __name__ == "__main__":
    sudoku_board = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]

    sudoku = Sudoku(sudoku_board)
    print(sudoku)
    sudoku.solve()
    print(sudoku)
