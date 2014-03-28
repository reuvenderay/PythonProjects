from math import hypot

__author__ = 'yosefderay'


class Board(object):

    def __init__(self, width, height, ships):
        super(Board, self).__init__()
        self.width = width
        self.height = height
        self.ships = ships
        self.grid = []

        for i in range(0, height):
            row = []
            for j in range(0, width):
                row.append(None)
            self.grid.append(row)

    def get_grid(self):
        return self.grid

    def all_sunk(self):
        return len(self.ships) == 0

    def fire(self, point):
        if point.row > self.height - 1 or point.column > self.width - 1 or point.row < 0 or point.column < 0:
            raise InvalidSelectionError()

        if self.grid[point.row][point.column] is not None:
            raise AlreadyGuessedError()

        for ship in self.ships:
            if ship.contains(point):
                point.point_type = Point.HIT
                self.grid[point.row][point.column] = point

                if ship.hit():
                    self.ships.remove(ship)
                    return FireResult.SINK

                return FireResult.HIT

        point.point_type = Point.MISS
        self.grid[point.row][point.column] = point
        return FireResult.MISS


class Point(object):
    HIT = 'hit'
    MISS = 'miss'
    GUESS = 'guess'

    def __init__(self, row, column):
        super(Point, self).__init__()
        self.point_type = None
        self.row = row
        self.column = column


class Ship(object):

    def __init__(self, point1, point2):
        super(Ship, self).__init__()
        self.point1 = point1
        self.point2 = point2
        self.hits = 0
        self.max_hits = self.__get_distance(point1, point2) + 1
        print self.max_hits

    def contains(self, point):
        return self.__get_distance(self.point1, point) + self.__get_distance(point, self.point2) + 1 == self.max_hits

    def hit(self):
        self.hits += 1
        if self.hits >= self.max_hits:
            return True
        return False

    def __get_distance(self, point1, point2):
        return hypot(point1.column - point2.column, point1.row - point2.row)


class AlreadyGuessedError(RuntimeError):
    pass


class InvalidSelectionError(OverflowError):
    pass


class FireResult(object):
    HIT = 'hit'
    MISS = 'miss'
    SINK = 'sink'
