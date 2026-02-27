import tkinter as tk
from tkinter import ttk, messagebox


class BlackjackUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game

        self.root.title("Blackjack")
        self.root.geometry("1300x600")
        self.root.resizable(False, False)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.bet_var = tk.StringVar(value="100")

        self.setup_widgets()
        self.create_card_slots()

    def setup_widgets(self):
        btn_style = ttk.Style()
        btn_style.configure("TButton", font=("Helvetica", 12))

        self.frame = ttk.Frame(self.root, padding=12)
        self.frame.grid(row=0, column=0, sticky="NSEW")

        for i in range(10):
            self.frame.grid_columnconfigure(5, minsize=60)

        self.balance_label = ttk.Label(
            self.frame, text=f"Balance: $1000", font=("Helvetica", 16, "bold")
        )
        self.balance_label.grid(
            row=0, column=0, columnspan=7, sticky="W", pady=5, padx=5
        )

        ttk.Label(self.frame, text="Your Hand", font=("Helvetica", 12)).grid(
            row=1, column=0, sticky="W", pady=(10, 2), padx=5
        )
        ttk.Label(self.frame, text="Dealer's Hand", font=("Helvetica", 12)).grid(
            row=1, column=6, sticky="W", pady=(10, 2), padx=5
        )

        self.player_value_label = ttk.Label(
            self.frame, text="Value: 0", font=("Helvetica", 14)
        )
        self.player_value_label.grid(row=1, column=4, sticky="S", pady=(10, 2), padx=5)

        self.dealer_value_label = ttk.Label(
            self.frame, text="Value: 0", font=("Helvetica", 14)
        )
        self.dealer_value_label.grid(row=1, column=9, sticky="S", pady=(10, 2), padx=5)

        self.hit_btn = ttk.Button(
            self.frame,
            text="Hit",
            command=self.on_hit,
            style="TButton",
        )
        self.hit_btn.grid(row=4, column=0, columnspan=2, sticky="EW", pady=20, padx=2)
        self.hit_btn.grid_configure(ipady=15)

        self.stand_btn = ttk.Button(
            self.frame,
            text="Stand",
            command=self.on_stand,
            style="TButton",
        )
        self.stand_btn.grid(row=4, column=2, columnspan=2, sticky="EW", pady=20, padx=2)
        self.stand_btn.grid_configure(ipady=15)

        self.dd_btn = ttk.Button(
            self.frame,
            text="Double Down",
            command=self.on_double_down,
            style="TButton",
        )
        self.dd_btn.grid(row=4, column=4, sticky="EW", pady=20, padx=2)
        self.dd_btn.grid_configure(ipady=15)

        self.bet_amount = ttk.Entry(
            self.frame, textvariable=self.bet_var, font=("Helvetica", 14)
        )
        self.bet_amount.grid(row=4, column=6, columnspan=2, sticky="EW", pady=10)

        self.bet_btn = ttk.Button(
            self.frame,
            text="Place Bet",
            command=self.on_place_bet,
            style="TButton",
        )
        self.bet_btn.grid(
            row=4, column=8, columnspan=2, sticky="EW", pady=10, padx=(10, 2)
        )

    def create_card_slots(self):
        self.player_card_labels = []
        self.dealer_card_labels = []

        empty_img = tk.PhotoImage(file="assets/empty.png")

        for i in range(5):
            label = ttk.Label(self.frame, image=empty_img)
            label.image = empty_img
            label.grid(row=2, column=i, sticky="W", pady=(16, 20), padx=2)

            self.player_card_labels.append(label)

        for i in range(4):
            label = ttk.Label(self.frame, image=empty_img)
            label.image = empty_img
            label.grid(row=2, column=(6 + i), sticky="W", pady=(16, 20), padx=2)

            self.dealer_card_labels.append(label)

    def update_balance(self, balance):
        pass

    def update_player_hand(self, hand):
        pass

    def update_dealer_hand(self, hand, hide_second_card=False):
        pass

    def update_player_value(self, value):
        pass

    def update_dealer_value(self, value):
        pass

    def load_card_image(self, card):
        pass

    def load_card_back(self):
        pass

    def reset_board(self):
        pass

    def set_player_controls(self, enabled):
        pass

    def set_bet_controls(self, enabled):
        pass

    def on_hit(self):
        pass

    def on_stand(self):
        pass

    def on_double_down(self):
        pass

    def on_place_bet(self):
        pass

    def refresh_ui(self):
        pass
