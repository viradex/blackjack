class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def __repr__(self):
        # For debugging
        return f"{self.rank} of {self.suit} with value {self.value}"
