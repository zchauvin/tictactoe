from typing import Optional, List, Sequence, Union

class Board:
    def __init__(self, n: int):
        self.n: int = n
        self.cells: List[str] = [''] * n * n
    
    def __str__(self) -> str:
        result = "\n"
        for i in range(self.n):
            for j in range(self.n):
                index = i * self.n + j
                result += f" {self.cells[index] or index + 1} "
                if j != self.n - 1:
                    result += '|'
            result += "\n"
            if i != self.n - 1:
                result += '-' * (4 * self.n - 1) + "\n"
        return result
    
    def has_player_won(self, character: str) -> bool:
        for line in self.get_lines():
            # check if all cells in the line match the given character
            if all(map(lambda i: self.cells[i] == character, line)):
                return True
        return False
    
    # zero-indexed
    def set(self, i: int, character: str) -> None:
        self.cells[i] = character
    
    def get_lines(self) -> List[List[int]]: 
        lines: List[List[int]] = []
        # add all horizontal/vertical lines
        for i in range(self.n):
            h_line = []
            v_line = []
            for j in range(self.n):
                h_line.append(self.n * i + j)
                v_line.append(i + self.n * j)
            lines += [h_line, v_line]

        forward_diagonal_line = []
        backward_diagonal_line = []
        for i in range(self.n):
            forward_diagonal_line.append(self.n * i + i)
            backward_diagonal_line.append(self.n * i + (self.n - i - 1))
        return lines + [forward_diagonal_line, backward_diagonal_line]
    
    # A move is valid if it falls within bounds and is not taken
    def is_valid_move(self, i: int) -> bool:
        return i >= 0 and i < self.n * self.n and not self.cells[i]
    
    def get_available_cells(self) -> List[int]:
        return list(filter(lambda i: not self.cells[i], range(self.n * self.n)))
    
    def copy(self):
        b = Board(self.n)
        b.cells = self.cells.copy()
        return b
    
    def is_full(self):
        return all(self.cells)
