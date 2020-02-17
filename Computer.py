from Player import Player
from Board import Board
from typing import List

class Computer(Player):
    def __init__(self, character: str, opponent_character: str):
        super().__init__(character)
        self.opponent_character = opponent_character

    def get_move(self, board: Board) -> int:
        scores = [float("-inf")] * board.n * board.n
        # for each possible move, associate the move's index with its max
        # score according to minimax recursion
        for i in board.get_available_cells():
            new_board = board.copy()
            new_board.set(i, self.character)
            scores[i] = self.__minimax(new_board, False)
        # return the index that maximizes the minimax score
        return scores.index(max(scores))
    
    def __minimax(self, board: Board, is_computer: bool) -> int:
        # check if the most recently placed character won, which is the opposite 
        # of the current player
        if board.has_player_won(self.opponent_character if is_computer else self.character):
            return -1 if is_computer else 1
        
        if board.is_full():
            return 0

        cells = board.get_available_cells()
        scores: List[int] = []
        # for each available move, calculate the recursive minimax score
        for i in cells:
            new_board = board.copy()
            new_character = self.character if is_computer else self.opponent_character
            new_board.set(i, new_character)
            scores.append(self.__minimax(new_board, not is_computer))

        # maximize if computer move, otherwise minimize
        return max(scores) if is_computer else min(scores)
