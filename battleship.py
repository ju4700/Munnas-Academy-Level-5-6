import random
from colorama import Fore, Style, init
init()


def print_board(board):
    print("   " + " ".join([str(i) for i in range(len(board))]))
    for i, row in enumerate(board):
        print(f"{i:2} " + " ".join(row))


def place_ship(board, size):
    while True:
        orientation = random.choice(["H", "V"])
        row = random.randint(0, len(board) - 1)
        col = random.randint(0, len(board[0]) - 1)

        if orientation == "H" and col + size <= len(board[0]):
            if all(board[row][c] == "~" for c in range(col, col + size)):
                for c in range(col, col + size):
                    board[row][c] = "S"
                return
        elif orientation == "V" and row + size <= len(board):
            if all(board[r][col] == "~" for r in range(row, row + size)):
                for r in range(row, row + size):
                    board[r][col] = "S"
                return


def main():
    print(Fore.CYAN + "Welcome to Advanced Battleship!" + Style.RESET_ALL)

    # Create a 10x10 board
    size = 10
    board = [["~"] * size for _ in range(size)]
    display_board = [["~"] * size for _ in range(size)]

    # Place ships (sizes 5, 4, 3, 2)
    ship_sizes = [5, 4, 3, 3, 2]
    for ship_size in ship_sizes:
        place_ship(board, ship_size)

    # Uncomment for debugging
    # for row in board:
    #     print(" ".join(row))

    turns = 20
    ships_left = len(ship_sizes)

    for turn in range(turns):
        print(Fore.YELLOW + f"\nTurn {turn + 1} of {turns}" + Style.RESET_ALL)
        print(Fore.GREEN + f"Ships remaining: {ships_left}" + Style.RESET_ALL)
        print_board(display_board)

        try:
            guess_row = int(input("Guess Row (0-9): "))
            guess_col = int(input("Guess Col (0-9): "))
        except ValueError:
            print(Fore.RED + "Invalid input! Please enter integers between 0 and 9." + Style.RESET_ALL)
            continue

        if not (0 <= guess_row < size and 0 <= guess_col < size):
            print(Fore.RED + "Out of bounds! Please choose valid coordinates." + Style.RESET_ALL)
            continue

        if display_board[guess_row][guess_col] != "~":
            print(Fore.RED + "You already guessed that spot!" + Style.RESET_ALL)
            continue

        if board[guess_row][guess_col] == "S":
            print(Fore.GREEN + "Hit! You hit a ship!" + Style.RESET_ALL)
            display_board[guess_row][guess_col] = Fore.RED + "X" + Style.RESET_ALL
            board[guess_row][guess_col] = "X"
            # Check if the ship is sunk
            sunk = True
            for r in range(size):
                for c in range(size):
                    if board[r][c] == "S":
                        sunk = False
                        break
            if sunk:
                ships_left -= 1
                print(Fore.CYAN + "You sank a ship!" + Style.RESET_ALL)
        else:
            print(Fore.BLUE + "Miss! No ship at this location." + Style.RESET_ALL)
            display_board[guess_row][guess_col] = Fore.BLUE + "O" + Style.RESET_ALL

        if ships_left == 0:
            print(Fore.GREEN + "\nCongratulations! You sank all the ships and won the game!" + Style.RESET_ALL)
            break
    else:
        print(Fore.RED + "\nGame Over! You ran out of turns." + Style.RESET_ALL)
        print(Fore.CYAN + "Here was the solution:" + Style.RESET_ALL)
        for r in range(size):
            for c in range(size):
                if board[r][c] == "S":
                    display_board[r][c] = Fore.RED + "S" + Style.RESET_ALL
        print_board(display_board)


if __name__ == "__main__":
    main()
