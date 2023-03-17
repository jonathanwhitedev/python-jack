"""
Designs and functions of playing cards including
suits and symbols for use in PythonJack
"""


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
