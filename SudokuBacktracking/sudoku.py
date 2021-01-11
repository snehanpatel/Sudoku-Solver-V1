def findEmpty(puzzle):
    # finds the next row, col that's not filled (-1)
    # return row, col tuple (or (None, None) if  there is none)

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
            
    return None, None

def checkValid(board, guess, row, col):
    # figures out whether the guess at the row/col of the board is a valid guess
    # returns True if is valid, False otherwise
    
    # check current row
    row_vals = board[row]
    if guess in row_vals:
        return False
    
    # check current column
    col_vals = [board[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    
    # and then current 3x3 the square
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    
    for r in range(row_start, row_start + 3):
        for c in range (col_start, col_start + 3):
            if board[r][c] == guess:
                return False
    
    return True

def solveBoard(board):
    # solve sudoku using backtracking
    # sudoku is represented as list of list, each nested list is a row
    # returns true of false regarding if solution exists
    # if solution exists, changes are made directly to list representing sudoku
    
    # finding empty square to make guess
    row, col = findEmpty(board)
    
    # if no empty squares, then sudoku is solved
    if row is None:
        return True
    
    # if there empty square, then iterate 1 and 9 as guesses
    for guess in range (1, 10):
        
        # check if number works
        if checkValid(board, guess, row, col):
            
            # if valid, then assign to correct index in list
            board[row][col] = guess
            
            # recurse using this board
            if solveBoard(board):
                return True
            
        # if not valid, then backtrack by assigning this square as empty
        board[row][col] = -1 # reset the guess
            
    # if no number combinations work, then unsolvable
    return False

if __name__ == '__main__':
    testboard = [
        [-1, -1, -1, 6, -1, -1, 7, -1, -1],
        [7, -1, 2, -1, 3, -1, -1, -1, 9],
        [-1, -1, -1, 8, 5, -1, -1, -1, 3],
        [-1, -1, 4, -1, -1, -1, -1, -1, 1],
        [5, 3, -1, -1, -1, -1, -1, 6, 8],
        [6, -1, -1, -1, -1, -1, 9, -1, -1],
        [3, -1, -1, -1, 4, 8, -1, -1, -1],
        [4, -1, -1, -1, 7, -1, 5, -1, 2],
        [-1, -1, 6, -1, -1, 1, -1, -1, -1]
    ]
    print(solveBoard(testboard))
    print(testboard)