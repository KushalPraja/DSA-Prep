def print_sudoku(grid):
  # Keep your existing print_sudoku function
  for i in range(9):
    if i % 3 == 0 and i != 0:
      print("-" * 21)
    for j in range(9):
      if j % 3 == 0 and j != 0:
        print("|", end=" ")
      print(grid[i][j] if grid[i][j] != 0 else ".", end=" ")
    print()

def isValidSudoku(board):
  # Each row must contain the digits 1-9 without duplicates.
  # Each column must contain the digits 1-9 without duplicates.
  # Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without duplicates.

  # loop trough "rows" and "columns" to check for duplicates

  for i in range(9):
    col=set()
    box=set()
    row=set()

    for j in range(9):
    if board[i][j]!=0
      if board[i,j] in col:
        return False




# Test cases - Example Sudoku boards
valid_sudoku = [
  [5,3,0,0,7,0,0,0,0],
  [6,0,0,1,9,5,0,0,0],
  [0,9,8,0,0,0,0,6,0],
  [8,0,0,0,6,0,0,0,3],
  [4,0,0,8,0,3,0,0,1],
  [7,0,0,0,2,0,0,0,6],
  [0,6,0,0,0,0,2,8,0],
  [0,0,0,4,1,9,0,0,5],
  [0,0,0,0,8,0,0,7,9]
]

invalid_sudoku = [
  [5,3,0,0,7,0,0,0,0],
  [6,0,0,1,9,5,0,0,0],
  [0,9,8,0,0,0,0,6,0],
  [8,0,0,0,6,0,0,0,3],
  [4,0,0,8,5,3,0,0,1], # Notice the duplicate 5 in this row
  [7,0,0,0,2,0,0,0,6],
  [0,6,0,0,0,0,2,8,0],
  [0,0,0,4,1,9,0,0,5],
  [0,0,0,0,8,0,0,7,9]
]

print("Valid Sudoku board:")
print(isValidSudoku(valid_sudoku))
print("\nInvalid Sudoku board:")
print(isValidSudoku(invalid_sudoku))
# Expected output:
# Valid Sudoku board:
# True
# Invalid Sudoku board:   
# False