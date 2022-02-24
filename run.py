import random

# opening statements and input
def welcome():
    print('Welcome to the game')
    player = input('Player Name: ')

# setting up of boards

def build_board(player_board):
    return [['O' for count in range(player_board)] for count in range(player_board)]
    build_board(10) 

def print_board(board):
    for b in board:
        print(*b)

board = build_board(10)

welcome()
print_board(board)



