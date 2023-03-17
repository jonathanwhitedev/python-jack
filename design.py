"""
Designs and functions of playing cards including
suits and symbols for use in PythonJack
"""
import collections
from typing import Sequence

Card = collections.namedtuple('Card', ['value', 'suit'])

YES_NO = 'yn'


def print_line(word: str) -> None:
    """Main print variable line"""
    print(f"♠ ♦ ♥ ♣ ════════════════════[{word}]════════════════════ ♣ ♥ ♦ ♠")


def validate_answer(question: str, choices: Sequence[str]) -> bool:
    """Answer validation"""
    while answer := input(question).lower():
        if answer in choices:
            return answer == choices[0]


def print_cards(cardlist):
    """Print cards in terminal with space)"""
    for card in zip(*cardlist):
        print('   '.join(card))


def print_card(*cards):
    """Print per turn of card in terminal with space)"""
    for line in zip(*cards):
        print('   '.join(line))


def reg_card_design(card):
    """Standard card design for main game"""
    suits = "Spades Diamonds Hearts Clubs".split()
    suit_symbols = ['♠', '♦', '♥', '♣']
    suit_pairs = dict(zip(suits, suit_symbols))

    v = card.value
    s = suit_pairs[card.suit]

    design = [

         '  ╔═════════╗',
        f'  ║{v:<5}    ║',
         '  ║         ║',
         '  ║         ║',
        f'  ║   {s:^3}   ║',
         '  ║         ║',
         '  ║         ║',
        f'  ║    {v:>5}║',
         '  ╚═════════╝'
    ]

    return design


facedown_design = [

     '  ╔═════════╗',
     '  ║░░░░░░░░░║',
     '  ║░░░░░░░░░║',
     '  ║░░░░░░░░░║',
     '  ║░░░░░░░░░║',
     '  ║░░░░░░░░░║',
     '  ║░░░░░░░░░║',
     '  ║░░░░░░░░░║',
     '  ╚═════════╝'
     ]

"""Hidden facedown playing card for dealer (normal casino rules)"""


def split_card_design(card):
    """Smaller card design for splits (for heroku game area)"""
    suits = "Spades Diamonds Hearts Clubs".split()
    suit_symbols = ['♠', '♦', '♥', '♣']
    suit_pairs = dict(zip(suits, suit_symbols))

    v = card.value
    s = suit_pairs[card.suit]

    design = [
         '╔══════╗',
        f'║ {v:<3}  ║',
         '║      ║',
        f'║  {s:>3} ║',
         '╚══════╝'
         ]

    return design
