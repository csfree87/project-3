# Variables for tic tac toe game

# Set board parameters
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

Count = 0
Place = "X"
Player = "X"

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
# check for winner, willcross check all directions using one function
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

def play_game():
    player = "X"
    count = 0
    while True:
        playing_board()
        global Score_x, Score_o

        if player == 'X' and count != 0:
            if win_check('O'):
                Score_o += 1
                print('O', 'wins')
                break

        elif player == 'O' and count != 0:
            if win_check('X'):
                Score_x += 1
                print('X', 'wins')
                break

        move = int(input(player + ", choose your spot 1-9: ")) - 1
        if (board[move]) == "-":
            board[move] = player
            count += 1
            if count == 9:
                print("Tie!")
                Score_x += 0
                Score_o += 0
                break
        else:
            print("That spot is taken. Try again")
        if player == "X":
            player = "O"
        else:
            player = "X"

# Play again
while True:
    print("To start game, select a number 1-9 to select spot on tic tac toe board win by placing three of the same in a row")

    play_game()
# Print welcome instructions
    
# Print score
    print("Player O gained " + str(Score_o) + " points")
    print("Player X gained " + str(Score_x) + " points")
# Reset gameboard
    board = ['-'] * 9

    if input("Play again (y/n): ") == "n":
        break
