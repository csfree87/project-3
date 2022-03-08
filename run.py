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

playing_board()