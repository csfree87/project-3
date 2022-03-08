# Variables
# Set board parameters
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

count = 0
place = "X"

# Score of players
score_x = 0
score_o = 0

# game functions

# set game board function


def playing_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# check for winner, willcross check all directions using one function
def win_check(win):
    if board[0] == board[1] == board[2] == win or \
        board[0] == board[4] == board[8] == win or \
        board[3] == board[4] == board[5] == win or \
        board[6] == board[7] == board[8] == win or \
        board[6] == board[4] == board[2] == win or \
        board[0] == board[3] == board[6] == win or \
        board[1] == board[4] == board[7] == win or \
            board[2] == board[5] == board[8] == win:
            return True
    else:
        return False


def play_game():
    spot = "X"
    count = 0
    while True:
        playing_board()
        global score_x, score_o

        if spot == 'X' and count != 0:
            if win_check('O'):
                score_o += 1
                print('O', 'wins')
                break

        elif spot == 'O' and count != 0:
            if win_check('X'):
                score_x += 1
                print('X', 'wins')
                break

        move = int(input(spot + ", choose your spot 1-9: ")) - 1
        if (board[move]) == "-":
            board[move] = spot
            count += 1
            if count == 9:
                print("Tie!")
                score_x += 0
                score_o += 0
                break
        else:
            print("That spot is taken. Try again")
        if spot == "X":
            spot = "O"
        else:
            spot = "X"


# Play again
while True:
    play_game()
# Print score
    print("Player O gained " + str(score_o) + " points")
    print("Player X gained " + str(score_x) + " points")
# Reset gameboard
    board = ['-'] * 9

    if input("Play again (y/n): ") == "n":
        break
