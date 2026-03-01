import random
from card import Card


class Deck:
    def __init__(self):
        self.reset()

    def create(self):
        ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        suits = ["S", "H", "D", "C"]

        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))

        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def deal(self):
        return self.cards.pop()

    def reset(self):
        self.cards = []
        self.create()
        self.shuffle()


if __name__ == "__main__":
    deck = Deck()
    print(deck.cards)
    print(len(deck.cards))
