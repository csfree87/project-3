# Variables for tic tac toe game

# Set board parameters
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

count = 0
place = "X"

# Player score
score_x = 0
score_o = 0

# Game functions

# Sets game board

def playing_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Will check for winner during game
def win_check(win):
    if board[0] == board[1] == board[2] == win or \
        board[0] == board[4] == board[8] == win or \
        board[0] == board[3] == board[6] == win or \
        board[1 == board[4] == board[7] == win or \
        board[2] == board[4] == board[6] == win or \
        board[2] == board[5] == board[8] == win or \
        board[6] == board[7] == board[8] == win or \
            board[3] == board[4] == board[5] == win:
            return True
    else:
        return False