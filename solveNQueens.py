def solveNQueens(n):
    def is_safe(row, col):
        return col not in cols and (row - col) not in diag1 and (row + col) not in diag2

    def backtrack(row):
        if row == n:
            # Found valid board
            board = [''.join(r) for r in current_board]
            solutions.append(board)
            return

        for col in range(n):
            if is_safe(row, col):
                # Place queen
                current_board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                # Remove queen (backtrack)
                current_board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

    solutions = []
    cols = set()      # Tracks columns with queens
    diag1 = set()     # Tracks "/" diagonals (row - col)
    diag2 = set()     # Tracks "\" diagonals (row + col)
    current_board = [['.' for _ in range(n)] for _ in range(n)]

    backtrack(0)
    return solutions

result = solveNQueens(4)
for sol in result:
    for row in sol:
        print(row)
    print("---")
