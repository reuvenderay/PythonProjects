__author__ = 'Reuven'
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)


def print_board(bord):
    for row in bord:
        print ' '.join(row)


print "Welcome to Mini-Battleship! You have ten turns \
to guess where my battleship is on this 5 by 5 square by guessing a row and a column."


ship_row = randint(1, 5)
ship_col = randint(1, 4)
second = ship_col + 1


print "Turn 1 of 10"
for turn in range(1, 11):
    print_board(board)
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Collumn:"))

    if guess_row not in range(1, 6) or guess_col not in range(1, 6):
        print "Oops, that's not even in the ocean."

    elif guess_row == ship_row and guess_col == ship_col:
        print "Hit!"
        board[guess_row - 1][guess_col - 1] = "S"

    elif guess_row == ship_row and guess_col == second:
        board[guess_row - 1][guess_col - 1] = "S"

    elif board[guess_row - 1][guess_col - 1] == "X":
        print "You guessed that one already."

    else:
        board[guess_row - 1][guess_col - 1] = "X"
        print "You missed my battleship!"

    if board[ship_row - 1].count("S") == 2:
        print "Sunk!"
        print "Congratulations! You sunk my battleship!"
        print_board(board)
        break

    if turn == 10:
        print "Game Over. So sorry. You lost."
        board[ship_row - 1][ship_col - 1] = "S"
        board[ship_row - 1][second - 1] = "S"
        print_board(board)
        break

    turn += 1
    print "Turn", turn, "of 10"