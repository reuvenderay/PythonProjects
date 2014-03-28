__author__ = 'Reuven'

from random import randint
from mini_battleship import Point, Ship, Board, ConsoleOutput, ConsoleInput, Executor

point1 = Point(randint(0, 4), randint(0, 3))
point2 = Point(point1.row, point1.column + 1)
ships = [Ship(point1, point2)]
executor = Executor(Board(5, 5, ships), ConsoleInput(), ConsoleOutput())
executor.execute(10)
