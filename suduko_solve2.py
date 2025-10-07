from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Track which numbers are used in each row, column, and box
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize sets with existing numbers on the board
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(val)

        def backtrack(r=0, c=0) -> bool:
            # If reached the end of rows, puzzle solved
            if r == 9:
                return True
            # Move to next row if column index exceeds
            if c == 9:
                return backtrack(r + 1, 0)
            # Skip filled cells
            if board[r][c] != ".":
                return backtrack(r, c + 1)

            box_index = (r // 3) * 3 + (c // 3)
            for num in map(str, range(1, 10)):
                if (
                    num not in rows[r]
                    and num not in cols[c]
                    and num not in boxes[box_index]
                ):
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

                    if backtrack(r, c + 1):
                        return True

                    # Undo changes (backtrack)
                    board[r][c] = "."
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_index].remove(num)

            # No valid number found, trigger backtrack
            return False

        backtrack()

num =[["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]]

solver = Solution()
solver.solveSudoku(num)