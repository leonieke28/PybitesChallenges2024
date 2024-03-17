from collections import namedtuple

SUITS = "Red Green Yellow Blue".split()

UnoCard = namedtuple("UnoCard", "suit name")


def create_uno_deck():
    """Create a deck of 108 Uno cards.
    Return a list of UnoCard namedtuples
    (for cards w/o suit use None in the namedtuple)"""
    numbers = list(range(0, 10))
    specials = ["Draw Two", "Skip", "Reverse"]
    colors = ["Red", "Green", "Yellow", "Blue"]
    wilds = ["Wild", "Wild Draw Four"]

    deck = []
    for color in colors:
        deck.append(UnoCard(color, str(numbers[0])))
        for number in numbers[1:] * 2:
            deck.append(UnoCard(color, str(number)))
        for special in specials * 2:
            deck.append(UnoCard(color, special))
    for wild in wilds * 4:
        deck.append(UnoCard(None, wild))
    return deck
