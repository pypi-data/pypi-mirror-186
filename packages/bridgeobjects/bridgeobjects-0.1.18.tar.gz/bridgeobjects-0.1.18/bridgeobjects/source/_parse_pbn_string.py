"""Helper functions for parsing pbn strings."""

from typing import Dict, List, Union, Tuple
import uuid
import re
import datetime

from .event import Event
from .board import Board
from .hand import Hand
from .card import Card
from .call import Call
from .trick import Trick
from .constants import CALLS, SEATS, CONTRACTS, CARD_NAMES
from ._file_constants import (PBN_CALL_CONVERSION, DEFAULT_EVENT_NAME,
                              DEFAULT_EVENT_DATE)


def parse_pbn(file_lines: List[str]) -> List[Event]:
    """Populate bridgeobjects objects from a pbn file."""
    current_name = None
    current_board_identifier = ""
    auction_state = False
    play_state = False
    board_state = False
    result_table = False
    board_index = 0
    events = []
    event = Event()
    board = Board()
    value = ''

    for line in file_lines:
        if line:
            tag = ""
            if line.startswith("%"):  # Comments
                pass
            elif line.startswith("[") or line.startswith("{"):
                (tag, value) = _parse_pbn_line(line)
                if auction_state and tag != 'Note':
                    auction_state = False
                elif play_state and tag != 'Note':
                    play_state = False
                elif result_table and tag != 'Note':
                    result_table = False
                elif line.startswith('{'):
                    if board_state and tag == 'Description':
                        board.description = value
                        board_state = False

            # Event event
            if tag == "Event":
                if not value:
                    value = str(uuid.uuid1())  # Dummy event
                if current_name != value:
                    current_name = value
                    current_board_identifier = ""
                    board_index = 0
                    if value and value != DEFAULT_EVENT_NAME:
                        event = Event(str(value))
                        events.append(event)

            # Event location
            elif tag == "Site":
                event.location = value

            # Event date
            elif tag == "Date":
                event.date = parse_date(value)

            # Scoring method
            elif tag == "Scoring":
                event.scoring_method = value

            # Board identifier
            elif tag == "Board":
                # Add dummy event in the case of a board only spec.
                if not events:
                    events.append(event)
                board_state = True
                if not value:
                    board_index += 1
                    value = str(board_index)
                board_identifier = value
                if current_board_identifier != board_identifier:
                    current_board_identifier = board_identifier
                    board = Board(board_identifier)
                    if not event:
                        event = Event(DEFAULT_EVENT_NAME)
                    if event not in events:
                        events.append(event)
                    event.boards.append(board)
                    trick_index = 0

            # Board Description
            elif tag == "Description":
                board.description = value

            # Board West
            elif tag == "West":
                board.west = value

            # Board North
            elif tag == "North":
                board.north = value

            # Board East
            elif tag == "East":
                board.east = value

            # Board South
            elif tag == "South":
                board.south = value

            # Board Dealer
            elif tag == "Dealer":
                board.dealer = value

            # Board Vulnerable
            elif tag == "Vulnerable":
                board.vulnerable = value

            # Board hands
            elif tag == "Deal":
                board.hands = _parse_pbn_deal(value)

            # Declarer
            elif tag == "Declarer":
                if value == '?':
                    value = ''
                board.contract.declarer = value
                board.declarer = value

            # Declarer
            elif tag == "Result":
                if value == '?':
                    value = -1
                if isinstance(value, int) or value.isnumeric():
                    board.declarers_tricks = int(value)

            # # Description
            # elif tag == "Description":
            #     board.description = value

            # Contract
            elif tag == "Contract":
                if value and value[-1] == 'X':
                    if value[-2] == 'X':
                        board.contract.modifier = 'R'
                        value = value[:-2]
                    else:
                        board.contract.modifier = 'D'
                        value = value[:-1]
                if value in CONTRACTS:
                    board.contract.name = value

            # Auction
            elif tag == "Auction":
                if value != 'None':
                    board.auction.first_caller = value
                auction_state = True
            elif auction_state:
                _parse_pbn_auction(board, tag, value, line)
                # board.auction.seat_calls = _get_seat_calls(board)


            # Play section
            elif tag == "Play":
                first_player = value
                play_state = True
            elif play_state:
                trick = _parse_pbn_play_section(board, tag, value, line,
                                                first_player)
                if trick.cards:
                    board.tricks.append(trick)
                    trick_index += 1
                first_player = trick.winner

            # Optimum results
            elif tag == "OptimumResultTable":
                result_table = True
            elif result_table:
                while '  ' in line:
                    line = line.replace('  ', ' ')
                result = line.split(' ')
                board.optimum_result_table[result[0]][result[1]] = result[2]
    return events


def _parse_pbn_line(line: str) -> Tuple[str, str]:
    """Return the tag and value from a pbn text line."""
    # example pbn line: [Site "Amsterdam, The Netherlands NLD"]
    line = line.strip()
    space_at = line.find(' ')
    tag = line[1:space_at]
    value = line[space_at + 1:]
    value = value[:-1]
    value = value.replace('"', '')
    return (tag, value)


def parse_date(value: str) -> datetime.date:
    """Return a datetime date object from a pbn date string."""
    # example date value: 2018.02.26
    is_valid = re.search("[0-9]{4}.[\0-9]{2}.[0-9]{2}", value)
    if is_valid:
        date_str = value.split('.')
        date = list(map(int, date_str))
        return datetime.date(date[0], date[1], date[2])
    else:
        return DEFAULT_EVENT_DATE


def _parse_pbn_deal(deal: str) -> Dict[object, Hand]:
    """Return a list of hands from a pbn deal string."""
    # example deal value:
    # N:K87.Q642.AJ6.K73 T5.85.Q752.Q6542 AQJ96.73.T843.JT 432.AKJT9.K9.A98
    hands: Dict[object, Hand] = {}
    # Assign hands to board in correct seat; 0 and 'N, 1 and 'E' etc..
    raw_hands = deal[2:].split(" ")
    first_seat = SEATS.index(deal[0])
    for index, card_list in enumerate(raw_hands):
        seat_index = (first_seat + index) % 4
        seat_name = SEATS[seat_index]
        hand = Hand(card_list)
        hands[seat_index] = hand
        hands[seat_name] = hand
    return hands


def _parse_pbn_auction(board: Board, tag: str, value: str, line: str):
    """Use the tag and value to update the board's auction attributes."""
    if tag == 'Note':
        note_line = value.split(':', 1)
        board.auction.notes[note_line[0]] = note_line[1]
    else:
        line = ' '.join(line.split())
        auction_line = line.split(' ')
        call_index = len(board.auction.calls) - 1
        for element in auction_line:
            if element in PBN_CALL_CONVERSION:
                element = PBN_CALL_CONVERSION[element]
            if element == '-':
                pass  # Dummy value in PBN. No bid has been made.
            elif element == 'A':
                passes = [Call('P')] * 4
                board.auction.calls = passes
            elif element in CALLS:
                board.auction.calls.append(Call(element))
                board.auction.note_keys.append('')
                call_index += 1
            elif element[0] == '=':
                board.auction.note_keys[call_index] = element.replace('=', '')
            else:
                raise ValueError(f'invalid element in calls: {element}')


def _parse_pbn_play_section(board: Board, tag: str, value: str, line: str,
                            first_player: str) -> Trick:
    """Use the tag and value to update the board's Tricks."""
    trick = Trick()
    note_found = False
    note_found = False
    card: Union[Card, None] = None
    if tag == 'Note':
        note_line = value.split(':', 1)
        board.play_notes[note_line[0]] = note_line[1]
    else:
        line = ' '.join(line.split())
        trick = Trick()
        play_line = line.split(' ')
        trick_note_keys: List[str] = []
        card_index = 0

        for element in play_line:
            if len(element) == 2:
                element = ''.join([element[1], element[0]])
            if element[0] == '=' and card:
                note_found = True
                trick_note_keys[card_index-1] = element.replace('=', '')
                card.play_note_index = element.replace('=', '')
            elif element in CARD_NAMES:
                card = Card(element)
                trick.cards.append(card)
                trick_note_keys.append('')
                card_index += 1
            trick.leader = first_player
            if len(trick.cards) == 4:
                trick.complete(board.contract.trump_suit)
        if note_found:
            trick.note_keys = [key for key in trick_note_keys]
    return trick

# def _get_seat_calls(board):
#     caller_index = SEATS.index(board.dealer)
#     seat_calls = {seat: [] for seat in SEATS}
#     for call in board.auction.calls:
#         seat_calls[SEATS[caller_index]].append(call)
#         caller_index += 1
#         caller_index %= 4
#     return seat_calls