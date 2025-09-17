# No longer using namedtuple to allow for mutable state (face_up)
SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
SUIT_ICONS = {'Spades': '♠', 'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣'}

# ANSI color codes
COLOR_RED = '\033[91m'
COLOR_RESET = '\033[0m'

class PlayingCard:
    def __init__(self, suit, rank, face_up=False):
        if suit not in SUITS:
            raise ValueError(f"Invalid suit: {suit}")
        if rank not in RANKS:
            raise ValueError(f"Invalid rank: {rank}")
        self.suit = suit
        self.rank = rank
        self.face_up = face_up

    def __repr__(self):
        if self.face_up:
            card_str = f"{self.rank.rjust(2)}{SUIT_ICONS[self.suit]}"
            if self.get_color() == 'Red':
                return f"{COLOR_RED}{card_str}{COLOR_RESET}"
            return card_str
        return " [X] " # Padded for alignment

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def get_color(self):
        if self.suit in ['Diamonds', 'Hearts']:
            return 'Red'
        else:
            return 'Black'

    def get_value(self):
        """Returns the numeric value of the card's rank."""
        return RANKS.index(self.rank) + 1

    def flip(self):
        """Flips the card over."""
        self.face_up = not self.face_up
