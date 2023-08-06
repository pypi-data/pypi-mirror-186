"""
    Helper functions for parsing lin strings.

    The lin format is proprietary see
        (https://www.bridgebase.com/forums/topic/46671-lin-file-format-description/)

    But this Ruby program
        (https://github.com/morgoth/lin/commit/2b75aa74a20cb8f872d454309f2f87af39292cc9)
     demonstrates how to parse a played board.


    The parse_lin function is intended to return the event from a lin file
    containing the boards for a tournament.

    The attributes seem to be contained in a pair of list elements,
    the first being an identifier, the second the value
    e.g.|sv|N| = {vulnerable: 'NS')

    The elements for a board all being on one line.
"""

from typing import Dict, List

from .event import Event
from .board import Board
from .suit import Suit
from .hand import Hand
from .card import Card
from .constants import SEATS
# from ._file_constants import
from ._file_constants import LIN_VULNERABILITY_CONVERSION
from ._parse_pbn_string import parse_date

from termcolor import colored
MODULE_COLOUR = 'red'


# TODO test for lin event
def parse_lin(file_text: List[str]) -> List[Event]:
    """Populate bridgeobjects objects from a lin file."""
    events = []
    event = Event()
    events.append(event)
    board_numbers = []
    board = None
    for line in file_text:
        if line:
            line_list = line.split('|')
            identifiers, values = line_list[::2], line_list[1::2]
            for identifier, value in zip(identifiers, values):
                if identifier == 'bn':
                    board_numbers = value.split(',')
                elif identifier == 'qx':
                    board = _parse_lin_board(identifiers, values)
                    event.boards.append(board)
    return events


def _parse_lin_board(identifiers: List[str], values: List[str]) -> Board:
    """Return a board object from a lin line."""
    board = Board()
    for identifier, value in zip(identifiers, values):
        if identifier == 'ah':
            board.identifier = value
        elif identifier == 'md':
            board.hands = _parse_lin_hands(value)
            dealer_index = (int(value[0]) - 3) % 4
            board.dealer = SEATS[dealer_index]
        elif identifier == 'sv':
            board.vulnerable = LIN_VULNERABILITY_CONVERSION[value]
    return board


def _parse_lin_hands(hands_string: str) -> Dict[object, Hand]:
    """Return a dict of hands from lin text."""
    hands: Dict[object, Hand] = {}
    dealer_index = (int(hands_string[0]))
    hand_index = (2 - dealer_index) % 4
    for hand_string in hands_string[1:].split(','):
        hand = Hand()
        for character in hand_string:
            if character in Suit.SHORT_NAMES:
                suit_name = character
            elif character == ',':
                hands[hand_index] = hand
                hands[SEATS[hand_index]] = hand
                hand = Hand()
                hand_index += 1
                hand_index %= 4
            else:
                card = Card(character, suit_name)
                hand.cards.append(card)
        hands[hand_index] = hand
        hand_index += 1
        hand_index %= 4

    hand = Hand()
    hand = Board.build_fourth_hand(hands)
    hands[hand_index] = hand
    hands[SEATS[hand_index]] = hand
    return hands
