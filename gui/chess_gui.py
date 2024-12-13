import tkinter as tk
from board import Board

class ChessGUI:
    def __init__(self, root):
        self.root = root
        self.board = Board()
        self.canvas = tk.Canvas(self.root, width=800, height=800)
        self.canvas.pack()
        self.selected_square = None
        self.hovered_square = None  # Track the square under the mouse
        self.square_size = 100
        self.draw_board()
        self.bind_events()

    def draw_board(self):
        """Render the chessboard grid and pieces."""
        self.canvas.delete("all")
        for row in range(8):
            for col in range(8):
                self.draw_square(row, col)

    def draw_square(self, row, col, highlight=False, hover=False):
        """Draw an individual square and any piece on it."""
        square_size = self.square_size
        x1, y1 = col * square_size, row * square_size
        x2, y2 = x1 + square_size, y1 + square_size
        color = "white" if (row + col) % 2 == 0 else "gray"

        # Highlight square on hover or selection
        if highlight:
            color = "lightblue"
        elif hover:
            color = "lightgreen"

        # Draw square
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

        # Draw piece (if present)
        square = self.board.grid[row][col]
        if square.piece:
            piece = square.piece
            piece_text = piece.name[0]  # First letter of piece name
            border_color = "black" if piece.color == "white" else "white"

            # Add piece border for contrast
            self.canvas.create_oval(
                x1 + 15, y1 + 15, x2 - 15, y2 - 15,
                fill="", outline=border_color, width=2
            )

            # Draw the piece text
            self.canvas.create_text(
                x1 + square_size // 2,
                y1 + square_size // 2,
                text=piece_text,
                fill="black" if piece.color == "white" else "white",
                font=("Arial", 24)
            )

    def bind_events(self):
        """Bind mouse events for hover and selection."""
        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.canvas.bind("<Button-1>", self.on_square_click)

    def on_mouse_move(self, event):
        """Handle mouse movement to highlight hovered square."""
        col = event.x // self.square_size
        row = event.y // self.square_size
        if 0 <= row < 8 and 0 <= col < 8:  # Ensure within bounds
            hovered_square = (row, col)
            if self.hovered_square != hovered_square:
                self.hovered_square = hovered_square
                self.redraw_hover_and_selected()

    def on_square_click(self, event):
        """Handle square selection on mouse click."""
        col = event.x // self.square_size
        row = event.y // self.square_size
        if 0 <= row < 8 and 0 <= col < 8:  # Ensure within bounds
            clicked_square = (row, col)
            if self.selected_square == clicked_square:
                # Deselect if clicking the same square
                self.selected_square = None
            else:
                self.selected_square = clicked_square
            self.redraw_hover_and_selected()

    def redraw_hover_and_selected(self):
        """Redraw the board, highlighting hovered and selected squares."""
        for row in range(8):
            for col in range(8):
                highlight = self.selected_square == (row, col)
                hover = self.hovered_square == (row, col)
                self.draw_square(row, col, highlight=highlight, hover=hover)

    def start(self):
        """Start the tkinter main loop."""
        self.root.mainloop()


# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    gui = ChessGUI(root)
    gui.start()
