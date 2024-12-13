class Piece:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def is_valid_move(self, start, end, board):
        raise NotImplementedError("Override this method in subclasses.")
