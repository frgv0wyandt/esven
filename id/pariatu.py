def print(board):
  """Prints the board to the console."""

  for row in board:
    for cell in row:
      print(cell, end=" ")
    print()
