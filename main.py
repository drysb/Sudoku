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
  for row in board:
    print_row = ""
    for num in row:
      print_row += (str(num) + " ")
    print(print_row)

#Find Empty Cell (Marked as 0)
def find_zero(board):
  for row_index, row in enumerate(board):
    for col_index, num in enumerate(row):
      if num == 0:
        return row_index, col_index  # Return indices of the first zero
  return None  # No zero found

