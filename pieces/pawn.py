from pieces.base_piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__("Pawn", color)

    def is_valid_move(self, start, end, board):
        row_diff = end[0] - start[0]
        col_diff = abs(end[1] - start[1])
        direction = 1 if self.color == "white" else -1

        # Standard move
        if col_diff == 0 and row_diff == direction:
            return board[end[0]][end[1]].is_empty()

        # Capture move
        if col_diff == 1 and row_diff == direction:
            return not board[end[0]][end[1]].is_empty()

        return False
