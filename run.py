import os
import random
from time import sleep

# ... (previously defined functions)

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
            board_player, board_computer, player_ships, computer_ships, guessed_locations = setup_game()
            break
        elif choice == "2":
            turns = 8
            board_player, board_computer, player_ships, computer_ships, guessed_locations = setup_game()
            break
        elif choice == "3":
            turns = 6
            board_player, board_computer, player_ships, computer_ships, guessed_locations = setup_game()
            break
        elif choice == "4":
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Please select a valid option")

    playing = True
    while playing:
        for turn in range(turns):
            print(f"Turn {turn + 1}")

            for ship_symbol in player_ships:
                display_boards(board_player, board_computer, "Place your ship: " + ship_symbol)
                place_ship(board_player, ship_symbol)
                clear()

            # Player's Turn
            player_turn(board_player, board_computer, computer_ships, guessed_locations)

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
