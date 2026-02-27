import tkinter as tk
from logic.game import BlackjackGame
from logic.ui import BlackjackUI


def main():
    root = tk.Tk()
    game = BlackjackGame()
    ui = BlackjackUI(root, game)

    root.mainloop()


if __name__ == "__main__":
    main()
