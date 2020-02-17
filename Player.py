from abc import ABC, abstractmethod
from Board import Board

class Player(ABC):
    def __init__(self, character):
        self.character = character
    
    @abstractmethod
    def get_move(self, board: Board) -> int:
        pass
