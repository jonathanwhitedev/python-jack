"""
PYTHON JACK GAME
"""
from __future__ import annotations
import random
import collections
import time
import os
from typing import Sequence
import subprocess as sp
import design
# IMPORT CARDS FROM DESIGN.PY


class Deck:
    """ deck class to set functions for game cards, decks, shuffles, draws """

    values = [str(v) for v in range(2, 11)] + list('JQKA')
    suits = "Spades Diamonds Hearts Clubs".split()
    suit_symbols = ['♠','♦','♥','♣']

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
        clear()
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


class Hand:
    """
    class to contain functions for calculating scores from hands 
    and functions to add/remove/hit cards to table.
    """

    def __init__(self):
        self.hand = []

    def __repr__(self):
        return "Hand()\n" + ''.join(f"({card.value}-{card.suit})" for card in self.hand)

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
        """Cards to display in hand"""
        card_list = [design.reg_card_design(card) for card in self.hand]
        design.print_cards(card_list)
        print(f"Card total of: {self.hand_score()}\n")

    def split_card_design(self):
        """Cards to display in split hand"""
        card_list = [design.split_card_design(card) for card in self.hand]
        design.print_cards(card_list)
        print(f"Card total of: {self.hand_score()}\n")


class Player(Hand):
    """
    class to contain functions for players hands
    calculating results of cards in play
    calculating chips betted with
    and validation steps for hit, stand, double down and splitting card selection.
    """

    def __init__(self, chips, bet=0, split_cards=False):
        super().__init__()
        self.chips = chips
        self.bet = bet
        self.profit = 0
        self.alive = True
        self.split_cards = split_cards
        self.has_blackjack = False

    def deal_cards(self, deck: Deck) -> None:
        """Check for blackjack or splits, print hand info"""
        self.hit(deck)
        self.hit(deck)
        print_line("Players Cards")
        self.card_design()
        self.has_blackjack = self.check_for_blackjack()
        self.split_cards = self.check_for_split()
        self.apply_split(deck)

    def add_chips(self, chips: float) -> None:
        """Chip winnings added"""
        self.chips += chips

    def remove_chips(self, chips: float) -> None:
        """Chip losses deducted"""
        self.chips -= chips

    def print_balance(self):
        """Chip balance printed"""
        print(f"\nYour chip balance is currently: ${self.chips:}\n")

    def check_for_blackjack(self):
        """Blackjack check for 21 in hand"""
        return len(self.hand) == 2 and self.hand_score() == 21

    def check_for_split(self):
        """Split check in hand"""
        if self.hand[0].value == self.hand[1].value:
            return validate_answer("Would you like to split your cards?: [y / n]: ".lower(), YES_NO)
        return False

    def wager(self):
        """Wager from chips for betting"""
        while True:
            self.print_balance()
            bet = input(f"How much would you like to bet?: $")
            if not bet.isdecimal() or str():
                print(("Sorry that was an invalid character, please enter a whole number (eg: 50)"))
                continue
            elif float(bet) > self.chips:
                print(f"Sorry, you don't have enough chips. Place a new amount between $1 - ${self.chips:}")
            else:
                self.bet = float(bet)
                self.remove_chips(float(bet))
                break

    def added_wager(self):
        """Wager from chips for additional betting (from splits/doubles)"""
        while True:
            self.print_balance()
            bet = input(f"How much additonal wager would you like to bet? ( ${self.bet} ) or less: $")
            if not bet.isdecimal() or float(bet) > self.bet:
                print("Please enter a whole number less or equal to you original bet")
                continue
            elif float(bet) > self.chips:
                print(f"You don't have enough chips to place this bet. Place a new amount between $1 - ${self.bet}")
            else:
                self.bet_two = float(bet)
                self.remove_chips(float(bet))
                break

    def confirm_double_down(self):
        """User validation to double down"""
        return validate_answer("\nYou will get only one more card. Please confirm selection for double down: [y / n] ".lower(), YES_NO)

    def double_down(self, deck: Deck) -> None:
        """Double down check"""
        self.added_wager()
        self.bet += self.bet_two
        self.design_move(deck)
        if self.hand_score() > 21:
            self.alive = False

    def apply_split(self, deck: Deck) -> None:
        """Split process to display to user"""
        if self.split_cards:
            self.added_wager()
            self.hand_two = Player(0, split_cards=True, bet=self.bet_two)
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
        """Hitting in split"""
        self.hit(deck)
        if self.split_cards:
            self.split_card_design()
        else:
            self.card_design()

    def player_move(self, deck: Deck) -> None:
        """User validation when cards are drawn"""
        while True:
            if self.hand_score() > 21 or self.has_blackjack:
                self.alive = False
                break
            if self.hand_score() == 21:
                break
            if len(self.hand) == 2:
                action = input("Would you like to hit, stand, or double-down? Enter [h, s, or d]: ").lower()
            else:
                action = input("Would you like to hit or stand: Enter [h or s]: ").lower()
            if action == 'd':
                if len(self.hand) == 2:
                    if self.confirm_double_down():
                        self.double_down(deck)
                        break
            if action == "h":
                self.design_move(deck)
            if action == "s":
                break

    def compute_results(self, dealer: Dealer) -> None:
        """Compute results from the round"""
        if self.alive and dealer.alive:
            if self.hand_score() > dealer.hand_score():
                print("YOU'RE A WINNER!\n")
                self.profit = 2
            elif self.hand_score() == dealer.hand_score():
                print("PUSH! THE DEALER HAS DRAWN THE SAME VALUE OF CARDS AS YOU\n")
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
        """Chips calculation"""
        self.add_chips(self.profit*self.bet)

    def reset(self):
        """Reset of game if 0 profit, draw"""
        self.hand = []
        self.alive = True
        self.split_cards = False
        self.profit = 0
        self.bet, self.bet_two = 0, 0


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
        facedown_card = design.facedown_design
        card_list = [facedown_card] + [design.reg_card_design(card) for card in self.hand[1:]]
        design.print_cards(card_list)


YES_NO = 'yn'

Card = collections.namedtuple('Card', ['value', 'suit'])
"""
Game controls and validations
"""


def clear():
    """Run function"""
    sp.run(('cls' if os.name == 'nt' else 'clear'), shell=True)


def validate_answer(question: str, choices: Sequence[str]) -> bool:
    """Answer validation"""
    while answer := input(question).lower():
        if answer in choices:
            return answer == choices[0]


def play_again() -> bool:
    """User validation after finished round to play again"""
    if validate_answer("Would you like to play another game of PythonJack? [y / n]: ".lower(), YES_NO):
        clear()
        return True
    return False


def print_line(word: str) -> None:
    """Main print variable line"""
    print(f"♠ ♦ ♥ ♣ ════════════════════[{word}]════════════════════ ♣ ♥ ♦ ♠")


def game():
    """Main game fixed rules, casino rules for decks, chip allocation and welcome line"""
    print_line('WELCOME TO PYTHONJACK')
    number_decks = 6
    player_chips = 1_000
    player = Player(player_chips)
    dealer = Dealer()
    deck = Deck(number_decks)

    deck.shuffle()

    while True:
        if player.chips == 0:
            print("You have lost all of your money. Game Over.")
            break
        print(f"Percentage of shoe not yet dealt: {len(deck)/(52*number_decks):.1%}")
        if deck.is_shuffle_time():
            deck.shuffle_time()

        player.wager()
        dealer.deal_cards(deck)
        player.deal_cards(deck)

        if not player.split_cards:
            player.player_move(deck)
            if player.alive:
                dealer.dealer_move(deck)
            player.compute_results(dealer)
        # SPLIT CARDS (Hands 1 and 2)
        else:
            if player.alive or player.hand_two.alive:
                dealer.dealer_move(deck)
            print("Hand One:")
            player.compute_results(dealer)
            print("Hand Two:")
            player.hand_two.compute_results(dealer)

            # Chips won by second hand: Added to total balance.
            player.chips += player.hand_two.chips

            player.print_balance()
        if play_again():
            player.reset()
            dealer.reset()
            continue
        else:
            break

    print("\nThanks for playing PythonJack. Please remember to gamble responsibly. \n")


if __name__ == "__main__":
    game()
