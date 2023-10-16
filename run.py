import random

# Initialize player and computer boards
board_player = [['-' for _ in range(5)] for _ in range(5)]
board_computer = [['-' for _ in range(5)] for _ in range(5)]

def print_board(board):
    for row in board:
        print(" ".join(row))

def place_ship(board, ship_symbol):
    while True:
        try:
            row = int(input(f"Enter the row to place your {ship_symbol} (0-4): "))
            col = int(input(f"Enter the column to place your {ship_symbol} (0-4): "))
            if 0 <= row <= 4 and 0 <= col <= 4 and board[row][col] == '-':
                return (row, col)
            else:
                print("Invalid placement. Try again.")
        except ValueError:
            print("Invalid input. Enter numbers between 0 and 4.")

# Place player's ships
print("Place your ships.")
for ship_symbol in ["S1", "S2", "S3"]:
    ship_row, ship_col = place_ship(board_player, ship_symbol)
    board_player[ship_row][ship_col] = ship_symbol
    print_board(board_player)

# Place computer's ships
print("Computer is placing its ships.")
for ship_symbol in ["S1", "S2", "S3"]:
    while True:
        ship_row = random.randint(0, 4)
        ship_col = random.randint(0, 4)
        if board_computer[ship_row][ship_col] == '-':
            board_computer[ship_row][ship_col] = ship_symbol
            break

player_ships = {"P1", "P2", "P3"}
computer_ships = {"C1", "C2", "C3"}

for turn in range(8):
    print(f"Turn {turn + 1}")
    # Player's Turn
    print_board(board_computer)  # Display the computer board
    print("Your turn")
    player_guess_row = int(input("Guess Row: "))
    player_guess_col = int(input("Guess Col: "))

    target = board_computer[player_guess_row][player_guess_col]
    if target in computer_ships:
        print(f"You hit a battleship!")
        board_computer[player_guess_row][player_guess_col] = "H"
        computer_ships.remove(target)
        print_board(board_computer)
    else:
        print("You missed!")
        print_board(board_computer)
        board_computer[player_guess_row][player_guess_col] = "X"

    if not computer_ships:
        print("You win! You've destroyed all of the computer's ships.")
        break  # Player wins, exit the loop

    # Computer Turn
    print_board(board_player)  # Display the player board
    print("Computer's Turn")
    while True:
        computer_guess_row = random.randint(0, 4)
        computer_guess_col = random.randint(0, 4)
        if board_player[computer_guess_row][computer_guess_col] not in {"H", "X"}:
            break

    target = board_player[computer_guess_row][computer_guess_col]
    if target in player_ships:
        print(f"Computer hit your battleship!")
        board_player[computer_guess_row][computer_guess_col] = "H"
        player_ships.remove(target)
        print_board(board_player)
    else:
        print("Computer missed!")
        board_player[computer_guess_row][computer_guess_col] = "X"
        print_board(board_player)

    if not player_ships:
        print("Computer wins! It has destroyed all of your ships.")
        break  # Computer wins, exit the loop
