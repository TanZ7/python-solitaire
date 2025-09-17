# This file will define the different piles used in Solitaire
# (e.g., Tableau, Foundation, Stock, Waste)

class Pile:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def __repr__(self):
        return f"{self.name} Pile with {len(self.cards)} cards"

    def add_card(self, card):
        """Adds a card to the pile."""
        self.cards.append(card)

    def get_top_card(self):
        """Returns the top card of the pile without removing it."""
        if not self.cards:
            return None
        return self.cards[-1]

    def deal(self):
        """Removes and returns the top card of the pile."""
        if not self.cards:
            return None
        return self.cards.pop()

    def deal_cards(self, num_cards):
        """Removes and returns a specified number of cards from the top."""
        if len(self.cards) < num_cards:
            return None
        cards_to_deal = self.cards[-num_cards:]
        self.cards = self.cards[:-num_cards]
        return cards_to_deal

    def add_cards(self, cards):
        """Adds a list of cards to the pile."""
        self.cards.extend(cards)

    def is_empty(self):
        return len(self.cards) == 0
