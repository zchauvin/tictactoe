from Player import Player
from Board import Board

class Human(Player):
    def get_move(self, board: Board) -> int:
        while True:
            try:
                selection = int(input(f'Where would you like to play? (1-{board.n * board.n}): ')) - 1
                if board.is_valid_move(selection):
                    return selection
            except ValueError:
                pass
            print('Invalid selection!')
