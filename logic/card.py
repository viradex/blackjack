class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    @property
    def value(self):
        if self.rank in ("J", "Q", "K"):
            return 10
        elif self.rank == "A":
            return 11  # decision on soft/hard is made later
        else:
            return int(self.rank)

    def get_path(self):
        return f"assets/{self.rank}/{self.rank}{self.suit}.png"

    def __repr__(self):
        return f"{self.rank}{self.suit}"
