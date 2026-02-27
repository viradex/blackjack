from .hand import Hand
from .deck import Deck


class Player:
    def __init__(self, name, balance=1000):
        self.name = name
        self.hand = Hand()
        self.balance = balance

    def hit(self, deck):
        pass

    def reset_hand(self):
        pass


class Dealer(Player):
    def should_hit(self):
        pass
