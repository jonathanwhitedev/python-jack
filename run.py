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
design.py file for card decoration in game
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

"""
class to contain functions for players hands
calculating results of cards in play
calculating chips betted with
and validation steps for hit, stand, double down and splitting card selection
"""

class Player(Hand):

    def __init__(self, chips, bet= 0, split_cards= False):
        super().__init__()
        self.chips = chips
        self.bet = bet
        self.profit = 0
        self.alive = True
        self.split_cards = split_cards
        self.has_blackjack = False

    def deal_cards(self, deck: Deck) -> None:
        self.hit(deck)
        self.hit(deck)
        print_line("Players Cards")
        self.card_design()
        self.has_blackjack = self.check_for_blackjack()
        self.split_cards = self.check_for_split()
        self.apply_split(deck)

    def add_chips(self, chips: float) -> None:
        self.chips += chips
    
    def remove_chips(self, chips: float) -> None:
        self.chips += chips

    def print_balance(self):
        print(f"\n Your chip balance is currently: ${self.chips:,.2f}\n")

    def check_for_blackjack(self):
        if self.hand[0].value == self.hand[1].value:
            return validate_answer("Do you want to split your cards?: [y / n]: ", YES_NO)
        return False

    def wager(self):
        while True:
            self.print_balance()
            bet = input(f"How much would you like to bet?: $")
            if not bet.isdecimal():
                continue
            elif float(bet) > self.chips:
                print("Sorry, you don't have enough chips. Place a new amount")
            else:
                self.bet = float(bet)
                self.remove_chips(float(bet))
                break

    def added_wager(self):
        while True:
            self.print_balance()
            bet = input(f"How much additonal wager would you like to bet? You may bet up to your original placed bet ${self.bet} or less: $")
            if not bet.isdecimal() or float(bet) > self.bet:
                continue
            elif float(bet) > self.chips:
                print("You don't have enough chips to place this bet. Place a new amount")
            else:
                self.bet_two = float(bet)
                self.remove_chips(float(bet))
                break
    
    def confirm_double_down(self):
        return validate_answer("\nYou will get only one more card. Please confirm selection for double down: [y / n] ", YES_NO)

    def double_down(self, deck: Deck) -> None:
        self.added_wager()
        self.bet += self.bet_two
        self.design_move(deck)
        if self.hand_score() > 21:
            self.alive = False
        
    def apply_split(self, deck: Deck) -> None:
        if self.split_cards:
            self.added_wager()
            self.hand_two = Player(0, split_cards= True, bet= self.bet_two)
            transfer_card = self.remove_card()
            self.hand_two.add_card(transfer_card)
            self.hit(deck)
            self.hand_two.hit(deck)

            print("\nFirst Hand: ")
            self.split_card_design()
            time.sleep(1)
            self.player_move(deck)
            print("\nSecond Hand: ")
            self.hand_two.split_card_design()
            time.sleep(1)
            self.hand_two.player_move(deck)
            time.sleep(1)

     def design_move(self, deck: Deck) -> None:
        self.hit(deck)
        if self.split_cards:
            self.split_card_design()
        else:
            self.card_design()

    def player_move(self, deck: Deck) -> None:
        while True:
            if self.hand_score() > 21 or self.has_blackjack:
                self.alive = False
                break
            if self.hand_score() == 21:
                break
            if len(self.hand) == 2:
                action = input("Would you like to hit, stand, or double-down? Enter [h, s, or d]: ")
            else:
                action = input("Would you like to hit or stand: Enter [h or s]: ")
            if action == 'd':
                if len(self.hand) == 2:
                    if self.confirm_double_down():
                        self.double_down(deck)
                        break
            if action == "h":
                self.visual_move(deck)
            if action == "s":
                break

    def compute_results(self, dealer: Dealer) -> None:
        if self.alive and dealer.alive:
            if self.hand_score() > dealer.hand_score():
                print("YOU'RE A WINNER!\n")
                self.profit = 2
            elif self.hand_score() == dealer.hand_score():
                print("PUSH!\n")
                self.profit = 1
            else:
                print("DEALER WINS!\n")

        elif not self.alive:
            if self.has_blackjack:
                print("BLACKJACK! WINNER!\n")
                self.profit = 2.5
            else:
                print("YOU HAVE BUST! YOU LOSE!\n")
        else:
            print("DEALER BUSTS! YOU WIN!\n")
            self.profit = 2
        self.settle()

    def settle(self):
        self.add_chips(self.profit*self.bet)

    def reset(self):
        self.hand = []
        self.alive = True
        self.split_cards = False
        self.profit = 0
        self.bet, self.bet_two = 0, 0


    