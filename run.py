import random

board = [['-' for _ in range(5)] for _ in range(5)]


def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ship(board):
    row = random.randint(0, 4)
    col = random.randint(0, 4)
    return (row, col)


print("Let's play Battleship!")
print_board(board)
ships = [(place_ship(board), place_ship(board), place_ship(board))]
print(ships)
guess_row = int(input("Guess Row: "))
guess_col = int(input("Guess Column: "))

if (guess_row, guess_col) in ships[0]:
        print("You sunk a battleship!")
        