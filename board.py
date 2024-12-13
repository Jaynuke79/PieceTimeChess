from pieces.base_piece import Piece
from pieces.pawn import Pawn

class Square:
    def __init__(self, piece=None):
        self.piece = piece

    def is_empty(self):
        return self.piece is None


class Board:
    def __init__(self):
        self.grid = self._initialize_board()

    def _initialize_board(self):
        grid = [[Square() for _ in range(8)] for _ in range(8)]

        # Initialize pawns
        for col in range(8):
            grid[1][col] = Square(Pawn("white"))
            grid[6][col] = Square(Pawn("black"))

        # Initialize other pieces similarly (example below)
        # grid[0][0] = Square(Rook("white"))

        return grid

    def move_piece(self, start, end):
        start_square = self.grid[start[0]][start[1]]
        end_square = self.grid[end[0]][end[1]]

        if start_square.is_empty():
            print("No piece at the starting position.")
            return False

        piece = start_square.piece
        if piece.is_valid_move(start, end, self.grid):
            end_square.piece = piece
            start_square.piece = None
            return True

        print("Invalid move.")
        return False
