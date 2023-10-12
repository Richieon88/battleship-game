from random import randint


board = []
for x in range(0, 6):
    board.append(["-"] * 6)

def print_board(board):
  for row in board:
    print(" ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_column(board):
  return randint(0, len(board[0]) - 1)


ship_row = random_row(board)
ship_column = random_column(board)

print_board(board)
print(ship_row)
print(ship_column)

guess_row = input("Guess ship row ")
guess_column = input("Guess shop column ")