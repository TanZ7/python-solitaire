from .data_structures.deck import Deck
from .data_structures.pile import Pile

class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        
        # Solitaire piles
        self.stock = Pile("Stock")
        self.waste = Pile("Waste")
        self.foundations = [Pile(f"Foundation {i+1}") for i in range(4)]
        self.tableau = [Pile(f"Tableau {i+1}") for i in range(7)]

    def setup_board(self):
        """
        Deals cards from the deck to the tableau piles.
        Only the top card of each tableau pile is face up.
        """
        for i in range(7):
            for j in range(i + 1):
                card = self.deck.deal()
                if card:
                    if j < i: # All cards except the last one are face down
                        card.face_up = False
                    self.tableau[i].add_card(card)
        
        # The rest of the deck goes to the stock pile, face down
        for card in self.deck.cards:
            card.face_up = False
        self.stock.cards = self.deck.cards
        self.deck.cards = [] # Clear the deck as it's now the stock
        print("Board has been set up.")

    def display_board(self):
        """
        Displays the current state of the game board.
        """
        print("\n" + "="*30)
        print("--- Foundations ---")
        for foundation in self.foundations:
            top_card = foundation.get_top_card()
            print(f"{foundation.name}: {top_card if top_card else '[Empty]'}")

        print("\n--- Tableau ---")
        # Display tableau piles horizontally for better readability
        max_len = max((len(p.cards) for p in self.tableau), default=0)
        
        # Print headers for tableau piles
        header = ""
        for i in range(len(self.tableau)):
            header += f"  T{i+1}   "
        print(header)
        print("-" * len(header))

        max_len = max((len(p.cards) for p in self.tableau), default=0)
        for i in range(max_len):
            row_str = ""
            for pile in self.tableau:
                if i < len(pile.cards):
                    card_str = str(pile.cards[i])
                    # Manually handle padding for strings with ANSI codes
                    # Visible length of a card is 3 (e.g., ' 9♠') or 5 for '[X]'
                    visible_len = 5 if not pile.cards[i].face_up else 3
                    padding = " " * (7 - visible_len)
                    row_str += card_str + padding
                else:
                    row_str += " " * 7
            print(row_str)


        print("\n--- Stock & Waste ---")
        print(f"Stock: {len(self.stock.cards)} cards ([X])")
        top_card = self.waste.get_top_card()
        print(f"Waste: {top_card if top_card else '[Empty]'}")
        print("="*40)

    def draw_card(self):
        """
        Draws a card from the stock to the waste pile.
        If the stock is empty, it refills from the waste pile.
        """
        if self.stock.is_empty():
            # Refill stock from waste
            print("Stock is empty. Refilling from waste pile...")
            self.stock.cards = self.waste.cards
            for card in self.stock.cards:
                card.face_up = False # All cards in stock are face down
            self.waste.cards = []
            return

        card = self.stock.deal()
        if card:
            card.face_up = True
            self.waste.add_card(card)
            print(f"Drew {card}")

    def validate_move_to_tableau(self, card, pile):
        """Checks if a card can be moved to a tableau pile."""
        if not card.face_up:
            return False # Cannot move face down cards

        if pile.is_empty():
            return card.get_rank() == 'K' # Only Kings on empty tableau
        
        top_card = pile.get_top_card()
        if not top_card.face_up:
            return False # Cannot place on a face down card

        return card.get_color() != top_card.get_color() and card.get_value() == top_card.get_value() - 1

    def validate_move_to_foundation(self, card, pile):
        """Checks if a card can be moved to a foundation pile."""
        if not card.face_up:
            return False

        if pile.is_empty():
            return card.get_rank() == 'A' # Only Aces on empty foundation

        top_card = pile.get_top_card()
        return card.get_suit() == top_card.get_suit() and card.get_value() == top_card.get_value() + 1

    def move_card(self, from_pile_str, to_pile_str, num_cards=1):
        source_pile_obj = None
        
        try:
            # --- Identify Source Pile ---
            from_pile_type = from_pile_str[0].lower()
            if from_pile_type == 'w':
                if num_cards > 1:
                    print("Cannot move more than one card from Waste.")
                    return
                source_pile_obj = self.waste
            elif from_pile_type == 't':
                from_pile_num = int(from_pile_str[1:]) - 1
                if not (0 <= from_pile_num < 7):
                    print("Invalid source tableau pile.")
                    return
                source_pile_obj = self.tableau[from_pile_num]
            else:
                print("Invalid source pile. Use 'w' (waste) or 't' (tableau).")
                return

            # --- Validate and Get Cards to Move ---
            if len(source_pile_obj.cards) < num_cards:
                print(f"Not enough cards on {from_pile_str}.")
                return

            cards_to_move = source_pile_obj.cards[-num_cards:]
            
            if any(not card.face_up for card in cards_to_move):
                print("Cannot move face-down cards in a stack.")
                return
            
            card_to_validate = cards_to_move[0] # The bottom card of the moving stack

            # --- Identify Destination and Validate Move ---
            to_pile_type = to_pile_str[0].lower()
            to_pile_num = int(to_pile_str[1:]) - 1

            if to_pile_type == 't' and 0 <= to_pile_num < 7:
                dest_pile = self.tableau[to_pile_num]
                if self.validate_move_to_tableau(card_to_validate, dest_pile):
                    moved_cards = source_pile_obj.deal_cards(num_cards)
                    dest_pile.add_cards(moved_cards)
                    print(f"Moved {num_cards} card(s) to Tableau {to_pile_num + 1}")
                else:
                    print("Invalid move to Tableau.")
                    return 
            elif to_pile_type == 'f' and 0 <= to_pile_num < 4:
                if num_cards > 1:
                    print("Cannot move more than one card to Foundation at a time.")
                    return
                dest_pile = self.foundations[to_pile_num]
                if self.validate_move_to_foundation(card_to_validate, dest_pile):
                    card = source_pile_obj.deal()
                    dest_pile.add_card(card)
                    print(f"Moved {card} to Foundation {to_pile_num + 1}")
                    if self.check_win_condition():
                        self.display_board()
                        print("\nCongratulations! You've won the game!")
                        return 'win'
                else:
                    print("Invalid move to Foundation.")
                    return
            else:
                print("Invalid destination pile.")
                return

            # --- Post-Move Actions (Flip Card) ---
            if from_pile_type == 't' and not source_pile_obj.is_empty() and not source_pile_obj.get_top_card().face_up:
                source_pile_obj.get_top_card().flip()
                print(f"Flipped card on {from_pile_str}: {source_pile_obj.get_top_card()}")

        except (ValueError, IndexError):
            print("Invalid pile format. Use 't1'-'t7', 'f1'-'f4', or 'w'.")

    def check_win_condition(self):
        """Checks if all cards are in the foundation piles."""
        return all(len(f.cards) == 13 for f in self.foundations)

    def start_game(self):
        print("Starting a new game of Solitaire...")
        self.setup_board()
        
        while True:
            self.display_board()
            action_input = input("\nEnter action (d, q, move [from] [to], move [from] [num] [to]): ").lower().split()

            if not action_input:
                continue

            command = action_input[0]

            if command == 'd':
                self.draw_card()
            elif command == 'q':
                print("Thanks for playing!")
                break
            elif command == 'move':
                result = None
                if len(action_input) == 3: # e.g., move t1 f1
                    from_pile = 'w' if action_input[1] == 'waste' else action_input[1]
                    result = self.move_card(from_pile, action_input[2], 1)
                elif len(action_input) == 4: # e.g., move t1 3 t2
                    try:
                        num = int(action_input[2])
                        result = self.move_card(action_input[1], action_input[3], num)
                    except ValueError:
                        print("Invalid number of cards.")
                else:
                    print("Invalid move command format.")
                
                if result == 'win':
                    break
            else:
                print("Invalid action.")
