"""
Player class for all rule's and functions
"""
import time
from hand import Hand
from deck import Deck
from design import print_line, validate_answer, YES_NO
from dealer import Dealer


class Player(Hand):
    """
    class to contain functions for players hands
    calculating results of cards in play
    calculating chips betted with
    and validation steps for hit, stand, double down 
    and splitting card selection.
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
            if float(bet) > self.chips:
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
            if float(bet) > self.chips:
                print(f"You don't have enough chips to place this bet. Place a new amount between $1 - ${self.bet}")
            else:
                self.bet_two = float(bet)
                self.remove_chips(float(bet))
                break

    def confirm_double_down(self):
        """User validation to double down"""
        return validate_answer("\nYou will get only one more card. Confirm selection for double down: [y / n] ".lower(), YES_NO)

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
