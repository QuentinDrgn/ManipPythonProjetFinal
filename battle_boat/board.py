import numpy as np

class Board:
    def __init__(self, board=None):
        self.board = board if board is not None else self.initialize_grid()

    def initialize_grid(self):
        grid = np.full((10, 10), ' ',dtype=str)
        return grid

    def print_grid(self):
        grid = self.board
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        print("   " + "   ".join([str(i) for i in range(10)]))
        print(" +" + "---+" * 10)
        for idx, row in enumerate(grid):
            print(f"{letters[idx]}| " + " | ".join(row) + " |")
            print(" +" + "---+" * 10)

    def get_cell(self, row, col):
        return self.board[row, col]
    
    def set_cell(self, row, col, value):
        self.board[row, col] = value

board_instance = Board()
board_instance.print_grid()