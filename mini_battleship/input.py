from mini_battleship.board import Point

__author__ = 'yosefderay'


class ConsoleInput(object):

    @staticmethod
    def get_point():

        guess_row = int(raw_input("Guess Row:")) - 1
        guess_col = int(raw_input("Guess Column:")) - 1
        point = Point(guess_row, guess_col)
        point.point_type = Point.GUESS
        return point
