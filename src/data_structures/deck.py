import random
from .card import PlayingCard, SUITS, RANKS

class Deck:
    def __init__(self):
        # All cards in a new deck start as face up for dealing purposes
        self.cards = [PlayingCard(suit, rank, face_up=True) for suit in SUITS for rank in RANKS]

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)
        print("Deck has been shuffled.")

    def deal(self):
        """Deals one card from the top of the deck."""
        if self.count() == 0:
            return None
        return self.cards.pop()
