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

"""
deck class to set functions for game cards, decks, shuffles, draws
"""
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

    #Shuffle when deck is less then < 50% full length
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

"""
class to contain functions for calculating scores from hands 
and functions to add/remove/hit cards to table.
"""
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

    def hit(self, deck: Deck) -> None:
        card = deck.draw_card()
        self.add_card(card)

    def hand_score(self) -> int:
        self.card_val = [10 if card.value in ['J','Q','K'] else 1 if card.value == 'A'
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
        card_list = [design.reg_card_design(card) for card in self.hand]
        design.print_cards(cardlist)
        print(f"\Total of: {self.hand_score()}\n")

class Player(Hand):

    def __init__(self, chips, bet= 0, split_cards= False):
        super().__init__()
        self.chips = chips
        self.bet = bet
        self.profit = 0
        self.alive = True
        self.split_cards = split_cards
        self.has_blackjack = False

    def deal_cards(self, deck, Deck) -> None:
        self.hit(deck)
        self.hit(deck)
        print_line("Players Cards")
        self.card_design()
        self.has_blackjack = self.check_for_blackjack()
        self.split_cards = self.check_for_split()
        self.apply_split(deck)