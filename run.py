from __future__ import annotations
import random
import collections
import time
import os
from typing import Sequence
import subprocess as sp 
import design

"""
PYTHONJACK GAME:
cards.py file for card decoration
"""



Card = collections.namedtuple('Card', ['value', 'suit'])

class Deck:

    values = [str(v) for v in range(2, 11)] + list('JQKA')
    suits = "Spades Diamonds Hearts Clubs".split()
    suit_symbols = ['♠','♦','♥','♣']

    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.cards = [Card(value, suit) for suit in self.suits for value in self.values] * self.num_decks
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
        return self.cards.pop()    

    def shuffle(self):
        random.shuffle(self.cards)

    #Shuffle when deck is < 50% full length
    def is_shuffle_time(self):
        return  len(self) < (self.length / 2)
   
    def shuffle_time(self):
        clear()
        print("Reshuffling the Deck...\n")
        time.sleep(1)
        self.reset()
        self.shuffle() 

    def reset(self):
        self.cards = [Card(value, suit) for suit in self.suits for value in self.values] * self.num_decks

    def deck_visual(self):
        s = [design.reg_card_design(card) for card in self.cards if card.suit == 'Spades']
        d = [design.reg_card_design(card) for card in self.cards if card.suit == 'Diamonds']
        h = [design.reg_card_design(card) for card in self.cards if card.suit == 'Hearts']
        c = [design.reg_card_design(card) for card in self.cards if card.suit == 'Clubs']
        design.print_cards(s)
        design.print_cards(d)
        design.print_cards(h)
        design.print_cards(c)   

class Hand:

    def __init__(self):
        self.hand = []

    def __repr__(self):
        return "Hand()\n" + ''.join(f"({card.value}-{card.suit})" for card in self.hand)

    def add_card(self, *cards: Card) -> None:
        for card in cards:
            self.hand.append(card)
    
    def remove_card(self):
        return self.hand.pop()