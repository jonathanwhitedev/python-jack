import time
from deck import Deck
from hand import Hand
from design import print_line, facedown_design, print_cards, reg_card_design


class Dealer(Hand):
    """
    class to contain functions for dealers rules of playing and dealing cards
    """

    def __init__(self):
        super().__init__()
        self.alive = True

    def deal_cards(self, deck: Deck) -> None:
        """Dealers cards for display"""
        self.hit(deck)
        self.hit(deck)
        print_line("Dealers Cards")
        self.dealer_design()
        time.sleep(1)

    def reset(self):
        """Reset of game"""
        self.hand = []
        self.alive = True

    def card_reveal(self):
        """Half second reveal between cards"""
        print_line("Dealers Cards")
        time.sleep(0.5)
        self.card_design()
        time.sleep(0.5)

    def dealer_move(self, deck: Deck) -> None:
        """Function to ensure dealer only plays to a max value of 17"""
        self.card_reveal()
        while True:
            if self.hand_score() in range(17, 22):
                break
            if self.hand_score() > 21:
                self.alive = False
                break
            if self.hand_score() < 17:
                self.hit(deck)
                time.sleep(1)
                self.card_design()

    def dealer_design(self):
        """Function to to hide first card facedown as per normal casion rules"""
        facedown_card = facedown_design
        card_list = [facedown_card] + [reg_card_design(card) for card in self.hand[1:]]
        print_cards(card_list)
