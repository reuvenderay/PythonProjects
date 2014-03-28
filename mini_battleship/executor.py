from mini_battleship import FireResult, InvalidSelectionError, AlreadyGuessedError

__author__ = 'yosefderay'


class Executor(object):

    def __init__(self, battleship_board, inputer, outputer):
        super(Executor, self).__init__()
        self.outputer = outputer
        self.battleship_board = battleship_board
        self.inputer = inputer

    def execute(self, max_turns):

        self.outputer.welcome(self.battleship_board)
        turns = 1
        while True:

            self.outputer.turn(turns, max_turns)
            self.outputer.grid(self.battleship_board.get_grid())

            try:
                result = self.battleship_board.fire(self.inputer.get_point())

                if result == FireResult.HIT:
                    self.outputer.hit()
                elif result == FireResult.SINK:
                    self.outputer.sink()
                else:
                    self.outputer.miss()
            except InvalidSelectionError:
                self.outputer.error("that's not even in the ocean.")
                continue
            except AlreadyGuessedError:
                self.outputer.error("You guessed that one already.")
                continue

            if self.battleship_board.all_sunk():
                self.outputer.won()
                break

            if turns == max_turns:
                self.outputer.lost()
                break

            turns += 1