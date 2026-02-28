class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def value(self):
        if self.rank in ("J", "Q", "K"):
            return 10
        elif self.rank == "A":
            return 11

        return int(self.rank)

    def __repr__(self):
        return f"{self.rank}{self.suit}"


if __name__ == "__main__":
    card = Card("A", "S")
    print(card.rank, card.suit, card.value, card, sep=", ")
