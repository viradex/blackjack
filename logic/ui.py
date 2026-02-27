import tkinter as tk
from tkinter import ttk, messagebox


class BlackjackUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game

        self.setup_widgets()
        self.create_card_slots()

    def setup_widgets(self):
        pass

    def create_card_slots(self):
        pass

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
