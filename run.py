import random

board_player = [['-' for _ in range(5)] for _ in range(5)]
board_computer = [['-' for _ in range(5)] for _ in range(5)]


def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ship(board):
    while True:
        try:
            row = int(input("Enter the row to place your ship (0-4): \n"))
            col = int(input("Enter the column to place your ship (0-4): \n"))
            if 0 <= row <= 4 and 0 <= col <= 4 and board[row][col] == '-':
                return (row, col)
            if 0 <= row <= 4 and 0 <= col <= 4 and board[row][col] == '-':
                return (row, col)
            else:
                print("Invalid placement. Try again.")
        except ValueError:
            print("Invalid input. Enter numbers between 0 and 4.")
   

print("Place your ships.")
for _ in range(3):
    ship_row, ship_col = place_ship(board_player)
    board_player[ship_row][ship_col] = "S"
    print_board(board_player)

print("Computer is placing its ships.")
for _ in range(3):
    ship_row, ship_col = place_ship(board_computer)

player_ships = set()
computer_ships = set()

for turn in range(8):
    print(f"Turn {turn + 1}")
    #Players Turn
    print("Your turn")
    guess_row = int(input("Guess Row: \n"))
    guess_col = int(input("Guess Col: \n"))
    
    if (guess_row, guess_col) in computer_ships[0]:
        print("You hit a battleship!")
        board_computer[guess_row][guess_col] = "H"
        computer_ships.remove((guess_row, guess_col))
        print_board(board_computer)
    else:
        print("You missed!")
        board_computer[guess_row][guess_col] = "H"
        print_board(board_computer)
    if not computer_ships:
        print("You win! You've destroyed all of the computer's ships.")
        break
    if not computer_ships:
        print("You win! You've destroyed all of the computer's ships.")
        break

    #Computer Turn
    Print("Computers Turn")
    guess_row = random.randint(0, 4)
    guess_col = random.randint(0, 4)

    if (guess_row, guess_col) in player_ships:
        print("Computer hit one of your battleships!")
        board_player[guess_row][guess_col] = "H"
        player_ships.remove((guess_row, guess_col))
        print_board(board_player)