# Name- Harleen Kaur
# Roll no.- 1025230010

# Project 1: Tic-Tac-Toe Game in Python
# This game is played by two players: X and O.

# All possible winning combinations (using list indexes)
WINNING_COMBINATIONS = [
    [0, 1, 2],  # First row
    [3, 4, 5],  # Second row
    [6, 7, 8],  # Third row
    [0, 3, 6],  # First column
    [1, 4, 7],  # Second column
    [2, 5, 8],  # Third column
    [0, 4, 8],  # Main diagonal
    [2, 4, 6]   # Other diagonal
]


def print_board(board):
    """Display the current Tic-Tac-Toe board."""
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    """Return True if the specified player has won."""
    for combination in WINNING_COMBINATIONS:
        if all(board[index] == player for index in combination):
            return True
    return False


def check_tie(board):
    """Return True if the board is full and nobody has won."""
    return " " not in board


def get_player_input(player, board):
    """Ask a player for a valid position between 1 and 9."""
    while True:
        choice = input(
            f"Player {player}, choose a position (1-9): "
        ).strip()

        # Check whether the input is a number
        if not choice.isdigit():
            print("Invalid input! Please enter a number.")
            continue

        position = int(choice)

        # Check whether the position is within the valid range
        if position < 1 or position > 9:
            print("Invalid position! Choose a number from 1 to 9.")
            continue

        # Convert the position to a list index
        index = position - 1

        # Check whether the selected position is empty
        if board[index] != " ":
            print("That position is already taken. Try again.")
            continue

        return index


def play_game():
    """Run one complete game of Tic-Tac-Toe."""
    # Create an empty board containing nine spaces
    board = [" "] * 9

    # Player X starts the game
    current_player = "X"

    print("==========================")
    print("\nWelcome to Tic-Tac-Toe!")
    print("==========================")
    print("Choose a position using the numbers 1 to 9.")
    print("The board positions are:")
    print_board([str(i) for i in range(1, 10)])

    # Continue until a player wins or the game is a tie
    while True:
        print_board(board)

        # Get a valid move from the current player
        position = get_player_input(current_player, board)

        # Place the player's symbol on the board
        board[position] = current_player

        # Check whether the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check whether all positions are filled
        if check_tie(board):
            print_board(board)
            print("It's a tie! The game is a draw.")
            break

        # Switch turns between X and O
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def main():
    """Main program: allow players to replay the game."""
    while True:
        play_game()

        while True:
            replay = input(
                "Would you like to play again? (yes/no): "
            ).strip().lower()

            if replay in ("yes", "y"):
                break
            elif replay in ("no", "n"):
                print("Thank you for playing Tic-Tac-Toe!")
                return  # Exits the function gracefully without system errors
            else:
                print("Invalid choice! Please enter yes or no.")


# Run the program
if __name__ == "__main__":
    main()