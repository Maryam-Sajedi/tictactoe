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


#print("Player " + choose_player() + " has chosen the marker " + choose_marker() + ".")

def assign_markers(player_1_name):
    player_1 = choose_marker(player_1_name)
    player_2 = "O" if player_1 == "X" else "X"
    print("Player 1's marker is " + player_1 + ".")
    print("Player 2's marker is " + player_2 + ".")
    return (player_1, player_2)   


def game():
    ### game starts here
    player_1 = player_name(1)
    player2 = player_name(2)
    markers = assign_markers(player_1)

    board = tictoctoe_board()
    display_board(board)

    #### rounds go here



# Tic-tac-toe game
if __name__ == "__main__":
    # Start a new round of Tic-tac-toe
    print("Welcome to a new round of Tic-Tac-Toe!")
    game()
