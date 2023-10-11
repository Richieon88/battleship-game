from random import randint


board = []
for x in range(0, 6):
    board.append(["-"] * 6)

def print_board(board):
    print(" ", " ".join("123456"))
    for letter, row in zip("ABCDEF", board):
        print(letter, " ".join(row))

def random_row(board):
  return randint(0, len(board) - 1)

def random_column(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_colunm = random_column(board)


