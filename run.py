import os
import random
from time import sleep

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def display_boards(player_board, computer_board, message):
    player_title = "Player's Board"
    computer_title = "Computer's Board"
    clear()
    print(f"{player_title:15}{' ' * 5}{computer_title}")
    for player_row, computer_row in zip(player_board, computer_board):
        player_row_str = ' '.join(player_row)
        computer_row_str = ' '.join(computer_row)
        print(f"{player_row_str:15}{' ' * 5}{computer_row_str}")
    print(message)

def player_turn(board_player, board_computer, computer_ships):
    display_boards(board_player, board_computer, "Your turn")
    player_guess_row, player_guess_col = validate_guess([])

    target = board_computer[player_guess_row][player_guess_col]
    print(target)
    if target in computer_ships:
        board_computer[player_guess_row][player_guess_col] = "H"
        computer_ships.remove(target)
        display_boards(board_player, board_computer, "You hit a battleship!")
    else:
        display_boards(board_player, board_computer, "You missed!")
        board_computer[player_guess_row][player_guess_col] = "X"

def computer_turn(board_player, board_computer, player_ships):
    display_boards(board_player, board_computer, "Computer's Turn")
    sleep(2)
    while True:
        computer_guess_row = random.randint(0, 4)
        computer_guess_col = random.randint(0, 4)
        if board_player[computer_guess_row][computer_guess_col] not in {"H", "X"}:
            break

    target = board_player[computer_guess_row][computer_guess_col]
    if target in player_ships:
        board_player[computer_guess_row][computer_guess_col] = "H"
        player_ships.remove(target)
        display_boards(board_player, board_computer, "Computer hit your battleship!")
        sleep(2)
    else:
        display_boards(board_player, board_computer, "Computer missed!")
        sleep(2)

def validate_guess(guesses_made):
    LINE_FLUSH = '\r\033[K'
    UP_FRONT_LINE = '\033[F'
    while True:
        while True:
            row = input("Guess Row: ")
            try:
                row = int(row)
            except ValueError:
                print(UP_FRONT_LINE + LINE_FLUSH + "Invalid input! Choose 0-4!")
                continue
            if row not in range(5):  # Change this range from 4 to 5 to allow entering '4'.
                print(UP_FRONT_LINE + LINE_FLUSH + "Invalid input! Choose 0-4!")
                continue
            break
        while True:
            col = input("Guess Column: ")
            try:
                col = int(col)
            except ValueError:
                print(UP_FRONT_LINE + LINE_FLUSH + "Invalid input! Choose 0-4!")
                continue
            if col not in range(5):  # Change this range from 4 to 5 to allow entering '4'.
                print(UP_FRONT_LINE + LINE_FLUSH + "Invalid input! Choose 0-4!")
                continue
            break
        if (row, col) in guesses_made:
            print(UP_FRONT_LINE + LINE_FLUSH + "You have already made this move")
            continue
        break
    return row, col

def main():
    board_player = [['-' for _ in range(5)] for _ in range(5)]
    board_computer = [['-' for _ in range(5)] for _ in range(5)]
    
    player_ships = ["P1", "P2", "P3"]
    computer_ships = ["C1", "C2", "C3"]
    playing = True
    
    while playing:
        turns = 8
        guesses = []

        # Place player's ships
        print("Place your ships.")
        for ship_symbol in player_ships:
            ship_row, ship_col = place_ship(board_player, ship_symbol)
            board_player[ship_row][ship_col] = ship_symbol
            display_boards(board_player, board_computer, "Place your ships.")

        # Place computer's ships
        print("Computer is placing its ships.")
        for ship_symbol in computer_ships:
            while True:
                ship_row = random.randint(0, 4)
                ship_col = random.randint(0, 4)
                if board_computer[ship_row][ship_col] == '-':
                    board_computer[ship_row][ship_col] = ship_symbol
                    break

        for turn in range(turns):
            print(f"Turn {turn + 1}")

            # Player's Turn
            player_turn(board_player, board_computer, computer_ships)

            if not computer_ships:
                print("You win! You've destroyed all of the computer's ships.")
                playing = False
                break

            # Computer Turn
            computer_turn(board_player, board_computer, player_ships)

            if not player_ships:
                print("Computer wins! It has destroyed all of your ships.")
                playing = False

    play_again = input("Do you want to play again? Y or N")
    if play_again.lower().startswith("y"):
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()