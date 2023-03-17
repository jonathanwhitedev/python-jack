"""
Hand class for all rule's and functions
"""
from design import Card
from deck import Deck
import design


class Hand:
    """
    class to contain functions for calculating scores from hands 
    and functions to add/remove/hit cards to table.
    """

    def __init__(self):
        self.hand = []

    def __repr__(self):
        return "Hand()\n" + ''.join(f"({card.value}-{card.suit})" 
        for card in self.hand)

    def add_card(self, *cards: Card) -> None:
        """Add card to back of hand"""
        for card in cards:
            self.hand.append(card)

    def remove_card(self):
        """remove card from hand"""
        return self.hand.pop()

    def hit(self, deck: Deck) -> None:
        """Add card after hit"""
        card = deck.draw_card()
        self.add_card(card)

    def hand_score(self) -> int:
        """scoring system for suits and Ace"""
        self.card_val = [10 if card.value in ['J', 'Q', 'K'] else 1 if card.value == 'A'
                         else int(card.value) for card in self.hand]

        self.card_scores = dict(zip(self.hand, self.card_val))
        score = 0
        for card in self.hand:
            card_score = self.card_scores[card]
            score += card_score
        if any(card.value == 'A' for card in self.hand) and score <= 11:
            score += 10

        return score

    def card_design(self):
        """Cards to display in hand"""
        card_list = [design.reg_card_design(card) for card in self.hand]
        design.print_cards(card_list)
        print(f"Card total of: {self.hand_score()}\n")

    def split_card_design(self):
        """Cards to display in split hand"""
        card_list = [design.split_card_design(card) for card in self.hand]
        design.print_cards(card_list)
        print(f"Card total of: {self.hand_score()}\n")
