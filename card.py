"""
Regular Playing Card function including suits and symbols for use in PythonJack
"""


def print_cards(cardlist):
    for card in zip(*cardlist):
            print('   '.join(card))

def print_card(*cards):
    for line in zip(*cards):
        print('   '.join(line))


def reg_card_visual(card):
    suits = "Spades Diamonds Hearts Clubs".split()
    suit_symbols = ['♠','♦','♥','♣']
    suit_pairs = dict(zip(suits, suit_symbols))

    v = card.value
    s = suit_pairs[card.suit]

    visual = [

         '  ╔════════════╗',
        f'  ║ {v:<5}      ║',
         '  ║            ║',
         '  ║            ║',
        f'  ║     {s:^3}    ║',
         '  ║            ║',
         '  ║            ║',
         '  ║            ║',
        f'  ║      {v:>5} ║',
         '  ╚════════════╝'
    ]

    return visual