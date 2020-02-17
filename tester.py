from Computer import Computer
from Board import Board 
import unittest

N = 3

class TestComputer(unittest.TestCase):
    def test_x_computer_never_loses(self):
        board = Board(N)
        c = Computer('x', 'o')
        self.helper(board, c, True)

    def test_o_computer_never_loses(self):
        board = Board(N)
        c = Computer('o', 'x')
        self.helper(board, c, False)
    
    # test to fuzz every possible human move after the computer takes the optimal move
    def helper(self, board: Board, c: Computer, is_computer_turn: bool) -> None:
        if is_computer_turn:
            self.assertFalse(
                board.has_player_won(c.opponent_character),
                'The computer\'s opponent must not have won'
            )
            # base case: tie game
            if board.is_full():
                return 

            # take the optimal computer move and recurse
            new_board = board.copy()
            new_board.set(c.get_move(board), c.character)
            self.helper(new_board, c, not is_computer_turn)
        else:
            # base case: computer win or tie game
            if board.has_player_won(c.character) or board.is_full():
                return
            # recurse on the human taking every possible move
            for cell in board.get_available_cells():
                new_board = board.copy()
                new_board.set(cell, c.opponent_character)
                self.helper(new_board, c, not is_computer_turn)
            
if __name__ == '__main__':
    unittest.main()
