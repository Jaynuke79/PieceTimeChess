import tkinter as tk
from gui.chess_gui import ChessGUI

def main():
    root = tk.Tk()
    gui = ChessGUI(root)
    gui.start()

if __name__ == "__main__":
    main()
