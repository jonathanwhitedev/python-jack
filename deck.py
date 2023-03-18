"""
Deck class for all rule's and functions
"""
import time
import random
from design import Card
import design


class Deck:
    """ deck class to set functions for game cards, decks, shuffles, draws """

    values = [str(v) for v in range(2, 11)] + list('JQKA')
    suits = "Spades Diamonds Hearts Clubs".split()
    suit_symbols = ['♠', '♦', '♥', '♣']

    def __init__(self, number_decks=1):
        self.number_decks = number_decks
        self.cards = [Card(value, suit) for suit in self.suits
        for value in self.values] * self.number_decks
        self.length = len(self)
        
    def __repr__(self):
        return "Deck()\n" + ''.join(f"({card.value}-{card.suit})" for card in self.cards)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def __setitem__(self, position, value):
        self.cards[position] = value

    def draw_card(self):
        """Card pop to draw cards"""
        return self.cards.pop()

    def shuffle(self):
        """Card shuffle for cards"""
        random.shuffle(self.cards)

    def is_shuffle_time(self):
        """Shuffle when deck is less then < 50% full length"""
        return len(self) < (self.length / 2)

    def shuffle_time(self):
        """Card shuffle print statment"""
        print("Reshuffling the Deck...\n")
        time.sleep(1)
        self.reset()
        self.shuffle()

    def reset(self):
        """Cards reset after shuffle"""
        self.cards = [Card(value, suit) for suit in self.suits
        for value in self.values] * self.number_decks

    def deck_visual(self):
        """Cards suits from design.py"""
        s = self.__get_cards__('Spades')
        d = self.__get_cards__('Diamonds')
        h = self.__get_cards__('Hearts')
        c = self.__get_cards__('Clubs')
        design.print_cards(s)
        design.print_cards(d)
        design.print_cards(h)
        design.print_cards(c)

    def __get_cards__(self, suit_name):
        return [design.reg_card_design(card) for card in self.cards
        if card.suit == suit_name]
