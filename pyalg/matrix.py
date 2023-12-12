def bf_find(matrix, elem):
    for row in matrix:
        for col in row:
            if col == elem:
                return True
    return False


def dc_find(matrix, elem):
    def _find(matrix, elem, row_start, row_end, col_start, col_end):
        if row_start > row_end or col_start > col_end:
            return False

        mid_row = (row_start + row_end) // 2
        mid_col = (col_start + col_end) // 2
        mid_element = matrix[mid_row][mid_col]

        if mid_element == elem:
            return True
        elif mid_element < elem:
            # Search in the bottom-right and top-right submatrices
            return _find(
                matrix, elem, row_start, row_end, mid_col + 1, col_end
            ) or _find(matrix, elem, mid_row + 1, row_end, col_start, mid_col)
        else:
            # Search in the top-left and bottom-left submatrices
            return _find(
                matrix, elem, row_start, row_end, col_start, mid_col - 1
            ) or _find(matrix, elem, row_start, mid_row - 1, col_start, col_end)

    if not matrix:
        return False

    rows = len(matrix)
    cols = len(matrix[0])

    return _find(matrix, elem, 0, rows - 1, 0, cols - 1)


if __name__ == "__main__":
    matrix = [[1, 2, 4, 7], [10, 15, 20, 47], [50, 92, 101, 102]]

    print(f"matrix: {matrix}")

    elem = 2

    in_matrix = dc_find(matrix, elem)

    print(f"{elem} in matrix: {in_matrix}")
