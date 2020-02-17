from Computer import Computer
from Board import Board 
import unittest
from typing import List

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

class TestBoard(unittest.TestCase):
    
    def test_player_has_not_won(self):
        self.has_player_won_helper([[], [0], [0, 1]], False)
    
    def test_player_has_won(self):
        self.has_player_won_helper([[0, 1, 2], [0, 3, 6], [0, 4, 8]], True)
    
    def has_player_won_helper(self, cases: List[List[int]], has_player_won: bool) -> None: 
        player = 'x'
        for cells in cases:
            b = Board(N)
            b.multi_set(cells, player)
            self.assertEqual(b.has_player_won(player), has_player_won)
    
    def test_get_lines(self):
        self.assertEqual(
            Board(N).get_lines(),
            [
                [0, 1, 2],
                [0, 3, 6],
                [3, 4, 5],
                [1, 4, 7],
                [6, 7, 8],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6]
            ]
        )
    
    def test_is_invalid_move(self):
        b = Board(N)
        occupied_cell = 0
        b.set(occupied_cell, 'x')
        for invalid_move in [-1, N * N, occupied_cell]:
            self.assertFalse(b.is_valid_move(invalid_move))

    def test_is_valid_move(self):
        b = Board(N)
        b.set(0, 'x')
        self.assertTrue(b.is_valid_move(1))

    def test_get_available_cells(self): 
        b = Board(N)
        expected = list(range(N * N))
        self.assertEqual(b.get_available_cells(), expected)
        b.set(0, 'x')
        b.set(1, 'o')
        self.assertEqual(b.get_available_cells(), expected[2:])
    
    def test_is_full(self):
        b = Board(N)
        self.assertFalse(b.is_full())
        b.set(0, 'x')
        self.assertFalse(b.is_full())
        b.multi_set(range(1, N * N), 'x')
        self.assertTrue(b.is_full())


if __name__ == '__main__':
    unittest.main()
