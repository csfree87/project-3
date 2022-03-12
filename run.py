# Variables for tic tac toe game

# Set board parameters
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Global variables
count = 0
Place = "X"
player = "X"

# Player score
Score_x = 0
Score_o = 0


# Game functions

# Sets game board


def playing_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Will check for winner during game, will check up and down, side to side,
# and diagonal
# check for winner, will cross-check all directions using one function
def win_check(win):
    if board[0] == board[1] == board[2] == win or \
            board[0] == board[4] == board[8] == win or \
            board[0] == board[3] == board[6] == win or \
            board[1] == board[4] == board[7] == win or \
            board[2] == board[5] == board[8] == win or \
            board[2] == board[4] == board[6] == win or \
            board[3] == board[4] == board[5] == win or \
            board[6] == board[7] == board[8] == win:
        return True
    else:
        return False


# Checks for a winner, ends the game if so.
def check_win():
    # Establishing global variables
    global count
    global Score_x
    global Score_o
    # The winner will always be the current player
    if player == 'X' and count != 0:
        if win_check('O'):
            Score_o += 1
            print('O', 'wins')
            return 1
    elif player == 'O' and count != 0:
        if win_check('X'):
            Score_x += 1
            print('X', 'wins')
            return 1


# Processes the player's move.
def player_move():
    # Establishing global variables
    global count
    global Score_x
    global Score_o
    # Retry variable to loop upon user error
    retry = 0
    while retry < 1 and count < 9:
        # Try catches empty input
        try:
            move = int(input(player + ", choose your spot 1-9: ")) - 1
        except ValueError:
            print("Invalid input.")
        # Else necessary to import move variable
        else:
            # 'if' statement ensures the value entered is 0-9 to catch IndexError
            if 0 <= move <= 9:
                if (board[move]) == "-":
                    board[move] = player
                    retry = 1
                    count += 1
                else:
                    print("That spot is taken. Try again")
            else:
                print("Invalid input.")
                # Return to while loop
    if count == 9:
        print("Tie!")
        Score_x += 0
        Score_o += 0

# Game play function


def play_game():
    global player
    while True:
        # Sets the board and score
        playing_board()
        global Score_x, Score_o

        # Checks for a victor before processing the next move
        if check_win() == 1:
            break
        player_move()

        # Swaps player for next move
        if player == "X":
            player = "O"
        else:
            player = "X"

# Play again
while True:
    print("To start game, select a number 1-9 to select spot on tic tac toe board") 
    print("win by placing three of the same in a row")

    play_game()
    # Print welcome instructions

    # Print score
    print("Player O gained " + str(Score_o) + " points")
    print("Player X gained " + str(Score_x) + " points")
    # Reset gameboard
    board = ['-'] * 9

    # Loops until valid response given
    PendingResponse = 0
    while PendingResponse == 0:
        again = input("Play again (y/n): ")
        if again == "y":
            PendingResponse = 1
        elif again == "n":
            quit()
        else:
            print("Invalid input")

    # X always goes first, and the count must be reset.
    count = 0
    player = "X"
