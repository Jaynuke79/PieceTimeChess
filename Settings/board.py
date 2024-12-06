import tkinter as tk

class ChessboardGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chessboard")
        self.canvas = tk.Canvas(self.window, width=800, height=800)
        self.canvas.pack()
        self.draw_board()

    def draw_board(self):
        square_size = 100
        for i in range(8):
            for j in range(8):
                color = "white" if (i+j) % 2 == 0 else "gray"
                self.canvas.create_rectangle(i*square_size, j*square_size, (i+1)*square_size, (j+1)*square_size, fill=color)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    gui = ChessboardGUI()
    gui.run()

