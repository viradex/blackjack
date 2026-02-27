from .card import Card


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        total = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == "A")

        while total > 21 and aces:
            total -= 10
            aces -= 1

        return total

    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21

    def is_bust(self):
        return self.get_value() > 21


if __name__ == "__main__":
    hand = Hand()

    hand.add_card(Card("H", "A"))
    hand.add_card(Card("H", "9"))
    hand.add_card(Card("H", "5"))

    print(hand.get_value())
    print(hand.is_blackjack())
    print(hand.is_bust())
