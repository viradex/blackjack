from card import Card


class Hand:
    def __init__(self):
        self.reset()

    def _eval_hand(self):
        """Internal method."""
        total = 0
        ace_count = 0

        for card in self.cards:
            total += card.value
            if card.rank == "A":
                ace_count += 1

        while total > 21 and ace_count > 0:
            total -= 10
            ace_count -= 1

        return {"total": total, "is_soft": ace_count > 0}

    def add_card(self, card):
        self.cards.append(card)
        return self.cards

    def get_value(self):
        return self._eval_hand()["total"]

    def is_bust(self):
        return self.get_value() > 21

    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21

    def is_soft(self):
        return self._eval_hand()["is_soft"]

    def reset(self):
        self.cards = []


if __name__ == "__main__":
    hand = Hand()
    hand.add_card(Card("A", "S"))
    hand.add_card(Card("7", "S"))
    hand.add_card(Card("10", "S"))
    print(hand.get_value())
    print(hand.get_value())
    print(hand.is_blackjack())
    print(hand.is_bust())
    print(hand.is_soft())
