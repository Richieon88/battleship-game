from random import randint

def build_board(dims):
    return [['-' for count in range(dims)] for count in range(dims)]

def print_board(board):
    for b in board:
        print(*b)

board = build_board(6)
print_board(board)           
