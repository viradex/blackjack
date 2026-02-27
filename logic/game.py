from .deck import Deck
from .player import Player, Dealer


class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Dealer("Dealer")

    def start_round(self):
        pass

    def player_hit(self):
        pass

    def player_stand(self):
        pass

    def player_double_down(self):
        pass

    def dealer_turn(self):
        pass

    def determine_winner(self):
        pass

    def reset_round(self):
        pass
