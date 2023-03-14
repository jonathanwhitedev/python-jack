from __future__ import annotations
import random
import collections
import time
import os
from typing import Sequence
import subprocess as sp 
import cards

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
        random.shuffle(self.cards)]