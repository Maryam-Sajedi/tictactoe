# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;)
# Python code for the game Tic-tac-toe, where two players take turns marking spaces in a 3×3 grid. 
# The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.    

# Function for creating an empty game board with 3X3 spots:

def tictoctoe_board():
    board = [[" " for col in range(3)] for row in range(3)]
    return board

# Function for display board:
def display_board(board=tictoctoe_board()):
    print("Updated Board:")
    print()
    for i, row in enumerate(board):
            print("  |".join(row))
            if i < 2:
                 print("---+---+---")
            

# Function for choosing a player:
def player_name(player_number):
    player = input(f"Please enter name of player {player_number}: ")
    return player

# Choose a marker:
def choose_marker(player_name):
     while True:
          marker = input(f"Choose a marker (X or O) for {player_name}: ")
          if marker == "X" or marker == "O":
               return marker
          else:
               print("Invalid input, please choose either 'X' or 'O'.")



def assign_markers(player_1_name, player_2_name):
    player_1 = choose_marker(player_1_name)
    player_2 = "O" if player_1 == "X" else "X"
    print(f"{player_1_name}'s marker is {player_1}.")
    print(f"{player_2_name}'s marker is {player_2}.")
    return (player_1, player_2)   


#Enter move: Player 1 starts:
def get_move(player, board, marker):
    while True:
        move = input(f"{player}, please enter your move (row and column) as 'row,col':")
        move = move.split(',')
        if len(move) != 2:
            print("Invalid input. Please enter your move in the format 'row,col'.")
            continue
        try:
            row, col = int(move[0]), int(move[1])
        except ValueError:
            print("Invalid input. Please enter numeric values for row and column.")
            continue 
        if row < 1 or row > 3 or col < 1 or col > 3:   
            print("Invalid move. Please enter values between 1 and 3 for both row and column.")
            continue
        row -= 1 # player inputs are 1-indexed, but our board is 0-indexed.
        col -= 1 
        if board[row][col] != " ":
            print("Invalid move. That spot is already taken. Please choose another spot.")
            continue  
        board[row][col] = marker 
        return (row, col)

# Function to check for a win:
def check_win(board, marker):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == marker:  # Check rows
            return True
        if board[0][i] == board[1][i] == board[2][i] == marker:  # Check columns
            return True
    if board[0][0] == board[1][1] == board[2][2] == marker:  # Check diagonal
        return True
    if board[0][2] == board[1][1] == board[2][0] == marker:  # Check anti-diagonal
        return True
    return False    
        
# Function to check for a draw:
def check_draw(board):
    for row in board:
        if " " in row:
            return False
        return True




 #### Game rounds go here:
def game():
    ### game starts here
    player_1 = player_name(1)
    player_2 = player_name(2)
    markers = assign_markers(player_1, player_2)

    board = tictoctoe_board()
    display_board(board)
    for i in range(9):
        player = player_1
        marker = markers[0]
        if i % 2 != 0:
            player = player_2
            marker = markers[1]
        move = get_move(player, board, marker) 
        display_board(board)
    
        winner = check_win(board, marker)
        if winner:
            print(f"Congratulations {player}! You have won the game!")
            break
        else:
            draw = check_draw(board)
            if draw:
                print("The game is a draw!")
                break


# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    game()
