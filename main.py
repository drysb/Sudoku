#Create Example Board
board = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]

#Print Current Board
def print_board(board):
    print("-------------------------")
    for row in board:
        print_row = "| "
        for num in row:
            print_row += (str(num) + " ")
            #Finds where to put vertical lines
            if (row.index(num) + 1) % 3 == 0:
               print_row += "| "
        #Finds where to put horizontal lines
        if (board.index(row) + 1) % 3 == 0 and board.index(row) != 8:
               print_row += "\n-------------------------"
        print(print_row)
    print("-------------------------")

print_board(board)

#Find Empty Cell (Marked as 0)
def find_zero(board):
  for row_index, row in enumerate(board):
    for col_index, num in enumerate(row):
      if num == 0:
        return row_index, col_index  # Return indices of the first zero
  return None  # No zero found

#Look to see if the placement of a number is valid
def is_valid(board, row, col, value):
  grid_row = (row // 3) + 1
  grid_column = (col // 3) + 1
  
  #Check for number in same row
  for num in board[row]:
    if num == value:
      return False
  
  #Check for number in same column
  for row in board:
    if row[col] == value:
      return False
  
  #Check 3x3 grid
  for row_index, row1 in enumerate(board):
    if ((row_index // 3) + 1) != grid_row:
      continue
    for col_index, num in enumerate(row1):
      if ((col_index // 3) + 1) != grid_column:
        continue
      if num == value:
        return False
  return True

def solve(board):
  #Base Case: There are no more 0s
    check = find_zero(board)
    if check is None:
        print("It is solved! Your solution is:")
        print("")
        print_board(board)
        return True
    else:
        row, col = check
    
  #There is a 0
    #Go through each number to see if it is valid
    for i in range(1,10):
        if is_valid(board,row, col, i):
            #Assigns number to board position
            board[row][col] = i
            #Run the solve function again with new value
            if solve(board):
              return True
            #Recursion hit a wall, set previous value back to 0 and try next number in for loop
            board[row][col] = 0    
    return False      

solve(board)
print_board(board)
