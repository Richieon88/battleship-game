from random import randint

board = [['-' for _ in range(5)] for _ in range(5)]


def print_board(board):
    for row in board:
        print(" ".join(row))

def place_battleship(board):
    row = random.randint(0, 4)
    col = random.randint(0, 4)
    return (row, col)

