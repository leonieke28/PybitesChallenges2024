from collections import namedtuple
import random

ACTIONS = ["draw_card", "play_again", "interchange_cards", "change_turn_direction"]
NUMBERS = range(1, 5)

PawCard = namedtuple("PawCard", "card action")


def create_paw_deck(n=8):
    cards = [f"{chr(i + 65)}{j + 1}" for i in range(n) for j in range(4)]
    actions = [None] * (n * 3) + ACTIONS * (n // 4)
    random.shuffle(actions)
    deck = [PawCard(card, action) for card, action in zip(cards, actions)]
    if n > 26:
        raise ValueError

    return deck
