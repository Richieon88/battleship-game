board = []
for x in range(0, 6):
    board.append(["-"] * 6)

def print_board(board):
    print(" ", " ".join("123456"))
    for letter, row in zip("ABCDEF", board):
        print(letter, " ".join(row))

print_board(board)