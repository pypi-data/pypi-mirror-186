"""Helper functions for parsing rbn strings."""

from typing import Dict, List, Tuple
import datetime

from .event import Event
from .board import Board
from .hand import Hand
from .call import Call
from .contract import Contract
from .auction import Auction
from .constants import RANKS, SEATS
from ._file_constants import PBN_VULNERABILITY_CONVERSION


def parse_rbn(file_text: List[str]) -> List[Event]:
    """Populate bridgeobjects objects from a rbn file."""
    events = []
    current_board_identifier = ""
    create_event = True
    board = Board()
    (north, south, west, east) = ("", "", "", "")
    for line in file_text:
        if line:
            tag = ""

            # Comments
            if line[0] == "%":
                pass

            # Notes
            if line[0] == "{":
                pass
            else:
                tag = line[0]
                value = line[2:]
                if tag in "EDL":
                    if create_event:
                        event = Event()
                        events.append(event)
                        create_event = False

                # Event name
                if tag == "E":
                    event.name = value

                # Event date
                elif tag == "D":
                    event.date = _parse_rbn_date(value)

                # Event location
                elif tag == "L":
                    event.location = value

                # Event Scoring
                elif tag == "F":
                    event.scoring_method = value

                # Board identifier
                elif tag == "B":
                    board_identifier = value
                    if current_board_identifier != board_identifier:
                        current_board_identifier = board_identifier
                        board = Board(board_identifier)
                        event.boards.append(board)
                        board.north, board.south, board.west, board.east = north, south, west, east
                    create_event = True

                # Board dealer and hands
                elif tag == "H":
                    board.dealer = value[0]
                    board.hands = _parse_rbn_deal(value)

                # Board auction and vulnerable
                elif tag == "A":
                    board.vulnerable = _get_rbn_vulnerable(value)
                    board.auction = _parse_rbn_auction(value)

                # Board contract and declarer
                elif tag == "C":
                    raw_data = value.split(':')
                    board.contract = _get_rbn_contract(raw_data[0])
                    if raw_data[1] == '?':
                        declarer = ''
                    else:
                        declarer = raw_data[1]
                    board.contract.declarer = declarer

                # Board players
                elif tag == "N":
                    (north, south, west, east) = _parse_rbn_seats(value)
                    (board.north, board.south, board.west, board.east) = \
                        (north, south, west, east)
        else:
            create_event = True
    return events


def _parse_rbn_deal(deal: str) -> Dict[object, Hand]:
    """Return a list of hands from a rbn deal string."""
    # example deal value:
    # W:A8765.QT.K9.AT87:J42.AJ7632.J.632:QT3.85.Q86.KQJ54:
    hands: Dict[object, Hand] = {}
    raw_hands = deal[2:].split(":")
    if len(raw_hands[3]) == 0:
        hand_list = _build_fourth_rpn_hand(raw_hands)
    else:
        hand_list = raw_hands
    first_seat = SEATS.index(deal[0])
    for index, card_list in enumerate(hand_list):
        seat_index = (first_seat + index) % 4
        seat_name = SEATS[seat_index]
        hand = Hand(card_list)
        hands[seat_index] = hand
        hands[seat_name] = hand
    return hands


def _parse_rbn_date(value: str) -> datetime.date:
    """Return a datetime date object from a pbn date string."""
    # example date value: 19930512
    year = int(value[:4])
    month = int(value[4:6])
    day = int(value[6:])
    return datetime.date(year, month, day)


def _parse_rbn_seats(value: str) -> Tuple[str, str, str, str]:
    """Return, north, south, west, east for an rbn file."""
    north, south, west, east = "", "", "", ""
    if value:
        pairs = value.split(":")
        if len(pairs) >= 1:
            north_south = pairs[0].split("+")
            if len(north_south) >= 1:
                north = north_south[0]
            if len(north_south) >= 2:
                south = north_south[1]
        if len(pairs) >= 2:
            west_east = pairs[1].split("+")
            if len(west_east) >= 1:
                west = west_east[0]
            if len(west_east) >= 2:
                east = west_east[1]
    return (north, south, west, east)


def _build_fourth_rpn_hand(raw_hands: List[str]) -> List[str]:
    """Build the fourth hand based on the other three hands."""
    used_cards: Dict[int, List[str]] = {
        0: [],
        1: [],
        2: [],
        3: [],
    }
    last_hand: Dict[int, List[str]] = {
        0: [],
        1: [],
        2: [],
        3: [],
    }
    # Create a list of cards used by other three hands.
    for hand in raw_hands[:-1]:
        suit_cards = hand.split('.')
        for suit, cards in enumerate(suit_cards):
            for card in cards:
                used_cards[suit].append(card)
    # Build a hand (as a list) from the cards not already used.
    for suit in range(4):
        for rank in reversed(RANKS[1:]):
            if rank not in used_cards[suit]:
                last_hand[suit].append(rank)
    # Convert list to string form.
    suit_names = []
    for index in range(4):
        suit_cards = last_hand[index]
        suit_names.append(('').join(suit_cards))
    fourth_hand = ('.').join(suit_names)
    raw_hands[3] = fourth_hand
    return raw_hands


def _get_rbn_vulnerable(value: str) -> str:
    """Return the auction vulnerability as a string."""
    return PBN_VULNERABILITY_CONVERSION[value[1]]


def _parse_rbn_auction(value: str) -> Auction:
    """Return the auction as a list of board.CALLS."""
    auction = Auction()
    pointer = 0
    calls = []
    while pointer < len(value):
        if value[pointer] == 'P':
            calls.append(Call('P'))
            pointer += 1
        elif value[pointer].isdigit():
            calls.append(Call(value[pointer:pointer + 2]))
            pointer += 2
        elif value[pointer] in 'XD':
            calls.append(Call('D'))
            pointer += 1
        elif value[pointer] == 'R':
            calls.append(Call('R'))
            pointer += 1
        elif value[pointer] == 'A':
            calls.extend([Call('P'), Call('P'), Call('P')])
            pointer += 1
        else:
            pointer += 1
    auction.calls = list(calls)
    return auction


def _get_rbn_contract(value: str) -> Contract:
    """Return the contract."""
    contract = Contract(name=value)
    return contract
