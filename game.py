import random

# Initialize the board with hyphens representing empty spots
def initialize_board():
    return [['-' for _ in range(3)] for _ in range(3)]

# Function to display the current state of the board
def show_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Function to check if the board is full
def is_board_full(board):
    for row in board:
        if '-' in row:
            return False
    return True

# Function to check if a player has won
def check_win(board, sign):
    # Check rows
    for row in board:
        if all([spot == sign for spot in row]):
            return True
    # Check columns
    for col in range(3):
        if all([board[row][col] == sign for row in range(3)]):
            return True
    # Check diagonals
    if all([board[i][i] == sign for i in range(3)]) or all([board[i][2-i] == sign for i in range(3)]):
        return True
    return False

# Function to start the game
def start_game():
    board = initialize_board()
    players = ['X', 'O']
    current_player = random.choice(players)

    print(f"Player {current_player} starts the game.\n")
    
    while True:
        show_board(board)
        print(f"Player {current_player}'s turn.")
        
        # Ask for row and column
        while True:
            try:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if row in range(3) and col in range(3) and board[row][col] == '-':
                    break
                else:
                    print("Invalid move. The spot is already taken or out of range. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers only.")
        
        # Update the board with the player's sign
        board[row][col] = current_player
        
        # Check if the current player has won
        if check_win(board, current_player):
            show_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (draw)
        if is_board_full(board):
            show_board(board)
            print("It's a draw!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
start_game()
