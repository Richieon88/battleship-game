import random

board_player = [['-' for _ in range(5)] for _ in range(5)]
board_computer = [['-' for _ in range(5)] for _ in range(5)]


def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ship(board):
    while True:
        try:
            row = int(input("Enter the row to place your ship (0-4): "))
            col = int(input("Enter the column to place your ship (0-4): "))
            if 0 <= row <= 4 and 0 <= col <= 4 and board[row][col] == '-':
                return (row, col)
            if 0 <= row <= 4 and 0 <= col <= 4 and board[row][col] == '-':
                return (row, col)
            else:
                print("Invalid placement. Try again.")
        except ValueError:
            print("Invalid input. Enter numbers between 0 and 4.")
   

print("Let's play Battleship!")
print_board(board)
ships = [(place_ship(board), place_ship(board), place_ship(board))]
print(ships)


for turn in range(4):
    print(f"Turn {turn + 1}")
    guess_row = int(input("Guess Row: \n"))
    guess_col = int(input("Guess Col: \n"))
    if (guess_row, guess_col) in ships[0]:
        print("You sunk a battleship!")
        board[guess_row][guess_col] = "0"
        print_board(board)
        ships[0] = [coord for coord in ships[0] if coord != (guess_row, guess_col)]
        if not ships[0]:
            print("All battleships destroyed! You win!")
            break
    else:
        if guess_row not in range(5) or guess_col not in range(5):
                print("Thats not even on the board")
        elif board[guess_row][guess_col] in ["X", "0"]:
            print("You already guessed that location.")
        else:
            print("You missed the battleships!")
            board[guess_row][guess_col] = "X"
            print_board(board)

    if turn == 3:
        print("Out of turns! Game Over.")        