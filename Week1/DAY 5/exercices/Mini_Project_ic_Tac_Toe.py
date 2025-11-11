# 🎮 TIC TAC TOE GAME
# ----------------------
# Key Concepts:
# - Lists (2D list)
# - Loops (while, for)
# - Conditional statements (if, elif, else)
# - Functions
# - User input

#  Step 1: Representing the Game Board
def create_board():
    """Create an empty 3x3 Tic Tac Toe board"""
    return [[" " for _ in range(3)] for _ in range(3)]


# 🎨 Step 2: Displaying the Game Board
def display_board(board):
    """Display the current state of the board"""
    print("\n" + "="*20)
    for i in range(3):
        print(" ", " | ".join(board[i]))
        if i < 2:
            print("  -----------")
    print("="*20 + "\n")


# 🎯 Step 3: Getting Player Input
def player_input(board, player):
    """Ask player for a move and validate input"""
    while True:
        try:
            position = int(input(f"Player {player}, enter a position (1-9): "))

            # Validate range
            if position < 1 or position > 9:
                print("❌ Please choose a number between 1 and 9.")
                continue

            # Convert position 1–9 to (row, col)
            row = (position - 1) // 3
            col = (position - 1) % 3

            # Validate if cell is empty
            if board[row][col] != " ":
                print("❌ That position is already taken. Try again.")
                continue

            return row, col

        except ValueError:
            print("⚠️ Invalid input. Please enter a number between 1 and 9.")


# 🏆 Step 4: Checking for a Winner
def check_win(board, player):
    """Check all winning combinations"""

    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# 🤝 Step 5: Checking for a Tie
def check_tie(board):
    """Check if all cells are filled (tie)"""
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

#  Step 6: Main Game Loop
def play():
    """Main game loop"""
    print("🎮 Welcome to Tic Tac Toe!")
    print("Positions on the board:")
    print("""
     1 | 2 | 3 
    ---+---+---
     4 | 5 | 6
    ---+---+---
     7 | 8 | 9
    """)
    print("Player X goes first.\n")

    # Initialize the board
    board = create_board()
    current_player = "X"

    # Game loop
    while True:
        display_board(board)

        # Get move
        row, col = player_input(board, current_player)
        board[row][col] = current_player

        # Check win
        if check_win(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins! 🎉")
            break

        # Check tie
        if check_tie(board):
            display_board(board)
            print("🤝 It's a tie! Nobody wins.")
            break

        # Switch player
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


# 🚀 Run the game
if __name__ == "__main__":
    play()
