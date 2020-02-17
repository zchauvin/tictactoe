from Player import Player
from Board import Board
from random import choice

class Computer(Player):
    def get_move(self, board: Board) -> int:
        return choice(board.get_available_cells())
