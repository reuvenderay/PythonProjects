__author__ = 'yosefderay'

from board import Point


class ConsoleOutput(object):

    def welcome(self, battleship_board):
        print "Welcome to mini_battleship! You have ten turns \
        to guess where my battleship is on this", battleship_board.width, "by", battleship_board.height, "square by guessing a row and a column."

    def grid(self, grid):

        for row in grid:
            print ' '.join([self.__get_point_output(point) for point in row])

    def hit(self):
        print "Hit!"

    def sink(self):
        print "Sunk!"

    def miss(self):
        print "You missed my battleship!"

    def lost(self):
        print "Game Over. So sorry. You lost."

    def won(self):
        print "Congratulations! You sunk all my battleships!"

    def error(self, message):
        print "Oops, " + message

    def turn(self, turn, max_turn):

        print "Turn", turn, "of", max_turn

    def __get_point_output(self, point):
        if point is None:
            return "O"
        if point.point_type == Point.HIT:
            return "S"
        if point.point_type == Point.MISS:
            return "X"