"""Processes to create a pbn event."""
import os

from typing import List
from .event import Event
from .board import Board
from .constants import SUIT_NAMES, RANKS, SEATS, DENOMINATION_NAMES
from ._file_constants import (PBN_VULNERABILITY_CONVERSION,
                              PBN_CALL_CONVERSION,
                              PBN_VERSION_TEXT, PBN_FORMAT_TEXT,
                              PBN_CONTENT_TEXT, PBN_CREATOR_TEXT,
                              RBN_VERSION_TEXT, RBN_CREATOR_TEXT)


def create_pbn_event_list(events: List[Event], path: str = '') -> List[str]:
    """Create a list of strings for events in pbn format."""
    output = []
    output = _append_pbn_header()
    if path:
        if not os.path.isfile(path):
            output = _append_pbn_header()
        else:
            with open(path, 'r') as pbn_file:
                for line in pbn_file.readlines():
                    line = line.replace('\n', '')
                    if len(line.replace(' ', '')) > 0:
                        if line[1] != '%':
                            output = _append_pbn_header()
                            break
                contents = pbn_file.readlines()
                if len(contents) == 0:
                    output = _append_pbn_header()
    for event in events:
        output.extend(_create_pbn_event(event))
    return output


def _create_pbn_event(event: Event) -> List[str]:
    """Return an event as string in pbn format as a list."""
    output = []
    output.append(f'[Event "{event.name}"]')
    output.append(f'[Site "{event.location}"]')
    if event.date:
        event_date = event.date.strftime('%Y.%m.%d')
        output.append(f'[Date "{event_date}"]')
    output.append('')
    for board in event.boards:
        output.extend(_create_pbn_board_list(board, event))
    return output


def _append_pbn_header() -> List[str]:
    """Create a list containing the pbn file header."""
    output = []
    output.append(PBN_VERSION_TEXT)
    output.append(PBN_FORMAT_TEXT)
    output.append(PBN_CONTENT_TEXT)
    output.append(PBN_CREATOR_TEXT)
    output.append('')
    return output


def create_pbn_board(board: Board) -> List[str]:
    board_list =  _create_pbn_board_list(board)
    return '\n'.join(board_list)


def _create_pbn_board_list(board: Board, event: Event = None) -> List[str]:
    """Return a board as a list of strings in pbn format."""
    output = [f'[Board "{board.identifier}"]']
    if board.description:
        output.append(f'[Description "{board.description}"]')
    if board.north:
        output.append(f'[North "{board.north}"]')
    if board.north:
        output.append(f'[East "{board.east}"]')
    if board.north:
        output.append(f'[South "{board.south}"]')
    if board.north:
        output.append(f'[South "{board.west}"]')

    output.append(f'[Dealer "{board.dealer}"]')
    if board.vulnerable:
        vulnerability = board.vulnerable.replace("Both", "All")
        output.append(f'[Vulnerable "{vulnerability}"]')
    output.append(f'[Deal "{board.dealer}:{_get_pbn_deal(board)}"]')
    if event:
        output.append(f'[Scoring {_question_from_null(event.scoring_method)}]')
    output.append(f'[Declarer {_question_from_null(board.contract.declarer)}]')

    if board.contract.call:
        if board.contract.declarer and board.contract.denomination:
            denomination = board.contract.denomination.name
            result = board.optimum_result_table[board.contract.declarer][denomination]
            if result:
                board.result = result
        question = _question_from_null(board.contract.call.name)
        output.append(f'[Contract {question}]')

    if board.auction.calls:
        output.extend(_create_pbn_auction(board))

    output.append(f'[Result {_question_from_null(board.result)}]')

    if board.tricks:
        output.extend(_create_pbn_play_section(board))

    if board.play_notes:
        for key in board.play_notes:
            note = f'[Note "{key}:{board.play_notes[key]}"]'
            output.append(note)

    # optimum result table
    results_tag = False
    for seat in SEATS:
        for denomination in DENOMINATION_NAMES:
            if board.optimum_result_table[seat][denomination]:
                if not results_tag:
                    output.append('[OptimumResultTable "Declarer;Denomination\\2R;Result\\2R"]')
                    results_tag = True
                    optimum_result = board.optimum_result_table[seat][denomination]
                output.append(f'{seat}{denomination:>3}{optimum_result:>3}')

    output.append('')
    return output


def _question_from_null(value: str) -> str:
    """Return a question mark if value is None or ''."""
    if not value:
        return "?"
    else:
        return value


def _get_pbn_deal(board: Board, delimiter: str = ' ') -> str:
    """Return a board's hands as a string in pbn format."""
    hands_list = []
    dealer_index = SEATS.index(board.dealer)
    for index in range(4):
        seat = (dealer_index + index) % 4
        hand = board.hands[seat]
        hand_list = []
        for suit_name in reversed(SUIT_NAMES):
            suit_cards = []
            for rank in reversed(RANKS[1:]):
                for card in hand.cards:
                    if card.name == ''.join([rank, suit_name]):
                        suit_cards.append(card.rank)
            hand_list.append(''.join(suit_cards))
        hands_list.append('.'.join(hand_list))
    return delimiter.join(hands_list)


def _create_rbn_event(event: Event) -> List[str]:
    """Return an event as string in rbn format as a list."""
    output = []
    output.append(f'E {event.name}')
    output.append(f'L {event.location}')
    if event.date:
        event_date = event.date.strftime('%Y%m%d')
        output.append(f'D {event_date}')
    output.append(f'M {_question_from_null(event.scoring_method)}')
    for board in event.boards:
        output.extend(_create_rbn_board(board))
    return output


def _create_pbn_auction(board: Board) -> List[str]:
    """Return an auction as a pbn list."""
    auction_list = ['[Auction "{}"]'.format(board.dealer)]
    """
        See PBN Spec at https://tistis.nl/pbn/

            In import format the player in the Auction tag value need not be
            the dealer.  For example, the calls are given in a table
            of 4 columns with West in the first column.  In that case, each
            player before the dealer has a hyphen ("-") in the first auction line.

        In this case, the player will be the dealer
    """
    line = []
    for call in board.auction.calls:
        if call.name in PBN_CALL_CONVERSION:
            pbn_call = PBN_CALL_CONVERSION[call.name]
        else:
            pbn_call = call.name
        line.append(pbn_call)
        if len(line) == 4:
            auction_list.append(' '.join([bid for bid in line]))
            line = []
    auction_list.append(' '.join([bid for bid in line]))
    return auction_list


def _create_pbn_play_section(board: Board) -> List[str]:
    """Return board's tricks as a pbn list."""
    trick_list = []
    player = board.tricks[0].leader
    trick_list.append('[Play "{}"]'.format(player))
    for trick in board.tricks:
        if trick.leader:
            line = []
            for index, card in enumerate(trick.cards):
                if card:
                    line.append(''.join([card.name[1], card.name[0]]))
                    if trick.note_keys[index]:
                        line.append('={}='.format(trick.note_keys[index]))
            trick_list.append(' '.join([card for card in line]))
    return trick_list


def create_rbn_list(events: List[Event]) -> List[str]:
    """Create a list of strings for events in rbn format."""
    output = []
    output.append(RBN_VERSION_TEXT)
    output.append(RBN_CREATOR_TEXT)
    for event in events:
        output.extend(_create_rbn_event(event))
    return output


def _create_rbn_board(board: Board) -> List[str]:
    """Return a board as a list of strings in pbn format."""
    output = [f'B {board.identifier}']

    #  names
    names = _create_rbn_names(board)
    if names:
        output.append(f'N {names}')

    # hands
    deal = _get_pbn_deal(board, ':')
    output.append('H {}:{}'.format(board.dealer, deal))

    # auction
    vulnerable = PBN_VULNERABILITY_CONVERSION[board.vulnerable]
    output.append('A {}{}:'.format(board.dealer, vulnerable))

    # contract
    board_contract = _question_from_null(board.contract.name)
    board_declarer = _question_from_null(board.declarer)
    contract = ':'.join([board_contract, board_declarer])
    if contract != "?:?":
        output.append(f'C {contract}')

    # result
    result = _question_from_null(board.result)
    if result != "?":
        output.append('[R result')
    output.append('')
    return output


def _create_rbn_names(board: Board) -> str:
    """Return the boards players in rbn format."""
    names = '{}+{}:{}+{}'.format(board.north, board.south,
                                 board.west, board.east)
    if names == "+:+":
        names = ""
    if names[:3] == "+:":
        names = names.replace("+:", ";")
    if names[-3:] == ":+":
        names = names.replace(":+", ";")
    return names


def _write_file(output: List[str], path: str, append: bool) -> bool:
    """Write the list 'output' to a text file defined by path."""
    if not os.path.isfile(path):
        with open(path, 'w') as f_clear_pbn_file:
            f_clear_pbn_file.write('')
    try:
        if append:
            mode = 'a'
        else:
            mode = 'w'
        with open(path, mode) as f_pbn_file:
            f_pbn_file.write('\n'.join(output))
        return True
    except FileNotFoundError as error:
        error_text = f'invalid file path: {path}. File not written'
        raise FileNotFoundError(error_text) from error
    return False
