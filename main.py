import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Blackjack")
root.geometry("1300x600")
root.resizable(False, False)
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

bet_var = tk.StringVar(value="100")

btn_style = ttk.Style()
btn_style.configure("TButton", font=("Helvetica", 12))

frame = ttk.Frame(root, padding=12)
frame.grid(row=0, column=0, sticky="NSEW")

for i in range(10):
    frame.grid_columnconfigure(5, minsize=60)

balance_label = ttk.Label(
    frame, text=f"Balance: $500", font=("Helvetica", 16, "bold")
)
balance_label.grid(row=0, column=0, columnspan=7, sticky="W", pady=5, padx=5)

ttk.Label(frame, text="Your Hand", font=("Helvetica", 12)).grid(
    row=1, column=0, sticky="W", pady=(10, 2), padx=5
)
ttk.Label(frame, text="Dealer's Hand", font=("Helvetica", 12)).grid(
    row=1, column=6, sticky="W", pady=(10, 2), padx=5
)

ttk.Label(frame, text="Value: 16", font=("Helvetica", 14)).grid(
    row=1, column=4, sticky="S", pady=(10, 2), padx=5
)
ttk.Label(frame, text="Value: 4", font=("Helvetica", 14)).grid(
    row=1, column=9, sticky="S", pady=(10, 2), padx=5
)

player_card_1 = tk.PhotoImage(file="assets/9/9S.png")
player_card_1_label = ttk.Label(frame, image=player_card_1)
player_card_1_label.grid(row=2, column=0, sticky="W", pady=(16, 20), padx=2)

player_card_2 = tk.PhotoImage(file="assets/7/7H.png")
player_card_2_label = ttk.Label(frame, image=player_card_2)
player_card_2_label.grid(row=2, column=1, sticky="W", pady=(16, 20), padx=2)

player_card_3 = tk.PhotoImage(file="assets/empty.png")
player_card_3_label = ttk.Label(frame, image=player_card_3)
player_card_3_label.grid(row=2, column=2, sticky="W", pady=(16, 20), padx=2)

player_card_4 = tk.PhotoImage(file="assets/empty.png")
player_card_4_label = ttk.Label(frame, image=player_card_4)
player_card_4_label.grid(row=2, column=3, sticky="W", pady=(16, 20), padx=2)

player_card_5 = tk.PhotoImage(file="assets/empty.png")
player_card_5_label = ttk.Label(frame, image=player_card_5)
player_card_5_label.grid(row=2, column=4, sticky="W", pady=(16, 20), padx=2)

dealer_card_1 = tk.PhotoImage(file="assets/4/4D.png")
dealer_card_1_label = ttk.Label(frame, image=dealer_card_1)
dealer_card_1_label.grid(row=2, column=6, sticky="W", pady=(16, 20), padx=2)

dealer_card_2 = tk.PhotoImage(file="assets/back/4.png")
dealer_card_2_label = ttk.Label(frame, image=dealer_card_2)
dealer_card_2_label.grid(row=2, column=7, sticky="W", pady=(16, 20), padx=2)

dealer_card_3 = tk.PhotoImage(file="assets/empty.png")
dealer_card_3_label = ttk.Label(frame, image=dealer_card_3)
dealer_card_3_label.grid(row=2, column=8, sticky="W", pady=(16, 20), padx=2)

dealer_card_4 = tk.PhotoImage(file="assets/empty.png")
dealer_card_4_label = ttk.Label(frame, image=dealer_card_4)
dealer_card_4_label.grid(row=2, column=9, sticky="W", pady=(16, 20), padx=2)

hit_btn = ttk.Button(
    frame,
    text="Hit",
    command=lambda: print("Hit"),
    style="TButton",
)
hit_btn.grid(row=4, column=0, columnspan=2, sticky="EW", pady=20, padx=2)
hit_btn.grid_configure(ipady=15)

stand_btn = ttk.Button(
    frame,
    text="Stand",
    command=lambda: print("Stand"),
    style="TButton",
)
stand_btn.grid(row=4, column=2, columnspan=2, sticky="EW", pady=20, padx=2)
stand_btn.grid_configure(ipady=15)

dd_btn = ttk.Button(
    frame,
    text="Double Down",
    command=lambda: print("Double down"),
    style="TButton",
)
dd_btn.grid(row=4, column=4, sticky="EW", pady=20, padx=2)
dd_btn.grid_configure(ipady=15)

bet_amount = ttk.Entry(frame, textvariable=bet_var, font=("Helvetica", 14))
bet_amount.grid(row=4, column=6, columnspan=2, sticky="EW", pady=10)

bet_btn = ttk.Button(
    frame,
    text="Place Bet",
    command=lambda: print(f"Submitted bet: ${bet_var.get()}"),
    style="TButton",
)
bet_btn.grid(row=4, column=8, columnspan=2, sticky="EW", pady=10, padx=(10, 2))

root.mainloop()
