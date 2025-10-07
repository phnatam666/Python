def isValidSudoku(board):
    rows = [set() for _ in range(9)]     # Track numbers in each row
    cols = [set() for _ in range(9)]     # Track numbers in each column
    boxes = [set() for _ in range(9)]    # Track numbers in each 3x3 box

    for i in range(9):          # Loop through rows
        for j in range(9):      # Loop through columns
            num = board[i][j]
            if num == ".":
                continue        # Skip empty cells

            box_index = (i // 3) * 3 + (j // 3)  # Calculate 3x3 box index

            # Check for duplicates
            if (num in rows[i] or
                num in cols[j] or
                num in boxes[box_index]):
                return False    # Duplicate found

            # Add the number to the sets
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_index].add(num)

    return True  # No duplicates found

num =[["5","3",".",".","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]] 

print(isValidSudoku(num))


