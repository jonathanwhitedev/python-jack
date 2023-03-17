"""
PYTHON JACK GAME
"""
from __future__ import annotations
import os
import subprocess as sp
from dealer import Dealer
from design import validate_answer, YES_NO
from player import Player
from deck import Deck
import design


# Game controls and validations


def clear():
    """Run function"""
    sp.run(('cls' if os.name == 'nt' else 'clear'), shell=True)


def play_again() -> bool:
    """User validation after finished round to play again or end"""
    if validate_answer("Press 'y' to replay or 'n'/enter key to exit: ", YES_NO):
        clear()
        return True
    return False


def game():
    """Main game fixed rules, casino rules for decks, chip allocation and welcome line"""
    design.print_line('WELCOME TO PYTHONJACK')
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
        break

    print("\nThanks for playing PythonJack. Please remember to gamble responsibly. \n")


if __name__ == "__main__":
    game()
