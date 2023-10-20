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
            row = int(
                input(
                    f"Enter the row to place your {ship_symbol} (0-4): "))
            col = int(
                input(
                    f"Enter the column to place your {ship_symbol} (0-4): "))
            if 0 <= row <= 4 and 0 <= col <= 4 and board[row][col] == '⬜':
                board[row][col] = ship_symbol
                return (row, col)
            else:
                print("Invalid placement. Try again.")
        except ValueError:
            print("Invalid input. Enter numbers between 0 and 4.")


def place_computer_ships(board, ships):
    for ship in ships:
        while True:
            row = random.randint(0, 4)
            col = random.randint(0, 4)
            if board[row][col] == '⬜':
                board[row][col] = ship
                break


def display_boards(player_board, computer_board, message, turns):
    player_title = "Player's Board"
    computer_title = "Computer's Board"
    clear()
    print(f"{player_title:15}{' ' * 5}{computer_title}")
    print(f"Turns left: {turns}")
    for player_row, computer_row in zip(player_board, computer_board):
        # for i, el in enumerate(computer_row):
        #     if el == "C1" or el == "C2" or el == "C3":
        #         computer_row[i] = "⬜"
        player_row_str = ' '.join(player_row)
        player_row_str = player_row_str.replace("P1", "🚢").replace("P2", "🚢").replace("P3", "🚢")
        computer_row_str = ' '.join(computer_row)
        computer_row_str = computer_row_str.replace("C1", "⬜").replace("C2", "⬜").replace("C3", "⬜")
        print(f"{player_row_str:15}{' ' * 5}{computer_row_str}")
    print(message)


def player_turn(
        board_player, board_computer, computer_ships, guessed_locations, turns
        ):
    display_boards(board_player, board_computer, "Your turn", turns)
    player_guess_row, player_guess_col = validate_guess(guessed_locations)

    target = board_computer[player_guess_row][player_guess_col]

    if (player_guess_row, player_guess_col) in guessed_locations:
        display_boards(
            board_player, board_computer,
            "You have already guessed this location!", turns)
    elif target in computer_ships:
        board_computer[player_guess_row][player_guess_col] = "✅"
        computer_ships.remove(target)
        guessed_locations.add((player_guess_row, player_guess_col))
        display_boards(board_player, board_computer,
                       "You hit a battleship!", turns)
    else:
        guessed_locations.add((player_guess_row, player_guess_col))
        display_boards(board_player, board_computer, "You missed!", turns)
        board_computer[player_guess_row][player_guess_col] = "❎"


def computer_turn(board_player, board_computer, player_ships, turns):
    display_boards(board_player, board_computer, "Computer's Turn", turns)
    sleep(2)
    while True:
        computer_guess_row = random.randint(0, 4)
        computer_guess_col = random.randint(0, 4)
        if board_player[computer_guess_row][computer_guess_col] not in {
                "✅", "❎"}:
            break

    target = board_player[computer_guess_row][computer_guess_col]
    if target in player_ships:
        board_player[computer_guess_row][computer_guess_col] = "✅"
        player_ships.remove(target)
        display_boards(board_player, board_computer,
                       "Computer hit your battleship!", turns)
        sleep(2)
    else:
        board_player[computer_guess_row][computer_guess_col] = "❎"
        display_boards(board_player, board_computer, "Computer missed!", turns)
        sleep(2)


def validate_guess(guessed_locations):
    LINE_FLUSH = '\r\033[K'
    UP_FRONT_LINE = '\033[F'
    while True:
        while True:
            row = input("Guess Row: ")
            try:
                row = int(row)
            except ValueError:
                print(
                    UP_FRONT_LINE + LINE_FLUSH + "Invalid input! Choose 0-4!"
                    )
                continue
            if row not in range(5):
                print(
                    UP_FRONT_LINE + LINE_FLUSH + "Invalid input! Choose 0-4!"
                    )
                continue
            break
        while True:
            col = input("Guess Column: ")
            try:
                col = int(col)
            except ValueError:
                print(
                    UP_FRONT_LINE + LINE_FLUSH + "Invalid input! Choose 0-4!"
                    )
                continue
            if col not in range(5):
                print(
                    UP_FRONT_LINE + LINE_FLUSH + "Invalid input! Choose 0-4!"
                    )
                continue
            break
        if (row, col) in guessed_locations:
            print(
                UP_FRONT_LINE + LINE_FLUSH + "You have already made this move"
                )
            continue
        break
    return row, col


def setup_game():
    guessed_locations = set()

    board_player = [['⬜' for _ in range(5)] for _ in range(5)]
    board_computer = [['⬜' for _ in range(5)] for _ in range(5)]

    player_ships = ["P1", "P2", "P3"]
    computer_ships = ["C1", "C2", "C3"]

    return (
        board_player, board_computer, player_ships,
        computer_ships, guessed_locations
    )


def main():
    while True:
        clear()
        print("Welcome to Battleship!")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print("4. Quit")
        choice = input("Enter the number of your choice: ")

        if choice == "1":
            turns = 10
            (
                board_player,
                board_computer,
                player_ships,
                computer_ships,
                guessed_locations
                ) = setup_game()
            break
        elif choice == "2":
            turns = 8
            (
                board_player,
                board_computer,
                player_ships,
                computer_ships,
                guessed_locations
                ) = setup_game()
            break
        elif choice == "3":
            turns = 6
            (
                board_player,
                board_computer,
                player_ships,
                computer_ships,
                guessed_locations
                ) = setup_game()
            break
        elif choice == "4":
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please select a valid option.")

    # Place the player's ships on the board
    for ship_symbol in player_ships:
        display_boards(board_player, board_computer,
                       f"Place your ship: {ship_symbol}", turns)
        place_ship(board_player, ship_symbol)
        clear()
        print_board(board_player)

    # Place the computer's ships on the board
    place_computer_ships(board_computer, computer_ships)

    playing = True
    turns_left = turns
    while playing:
        for _ in range(turns):
            if turns_left == 0:
                display_boards(
                    board_player, board_computer,
                    "You are out of turns! Game Over!", turns_left)
                playing = False
                break
            # print(f"Turn {turn + 1}")

            # Player's Turn
            player_turn(board_player, board_computer,
                        computer_ships, guessed_locations, turns_left)
            turns_left -= 1
            # print_board(board_player)

            if not computer_ships:
                display_boards(
                    board_player, board_computer,
                    "You win! You've destroyed all of the computer's ships.",
                    turns_left)
                playing = False
                break

            # Computer Turn
            computer_turn(board_player, board_computer,
                          player_ships, turns_left)
            # print_board(board_player)

            if not player_ships:
                display_boards(
                    board_player, board_computer,
                    "Computer wins! It has destroyed all of your ships.",
                    turns_left)
                # print("Computer wins! It has destroyed all of your ships.")
                playing = False
                break

    play_again = input("Do you want to play again? Y or N: ")
    if play_again.lower().startswith("y"):
        main()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    main()