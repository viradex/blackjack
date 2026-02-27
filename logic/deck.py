import random
from .card import Card


class Deck:
    def __init__(self):
        self.rebuild()

    def build(self):
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["H", "D", "C", "S"]

        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def deal(self):
        return self.cards.pop()

    def rebuild(self):
        self.cards = []
        self.build()
        self.shuffle()


if __name__ == "__main__":
    deck = Deck()
    print(deck.build())
    print(deck.shuffle())
    print(deck.deal())
    print(len(deck.cards))
