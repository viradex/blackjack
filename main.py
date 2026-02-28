import tkinter as tk
from ui import BlackjackUI


def main():
    root = tk.Tk()
    ui = BlackjackUI(root)

    root.mainloop()


if __name__ == "__main__":
    main()
