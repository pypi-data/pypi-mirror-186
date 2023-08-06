"""A class to represent a bridgeobjects Trick."""

import json
from typing import List, Union

from .constants import SEATS, CARD_NAMES
from .card import Card
from .suit import Suit


__all__ = ['Trick',]


class Trick(object):
    """A trick object for the board player."""
    def __init__(self, cards: Union[List[Card], None]=None):
        self._initialise(cards)
        self._leader = ''
        self.winner = ''
        self.note_keys = ['' for _ in range(4)]

    def _initialise(self, cards):
        """Initialise the class."""
        if not cards:
            cards = []
        self._cards = self._card_setter(cards) # a list of Card instances
        if self.cards:
            self._start_suit = self._cards[0].suit
        else:
            self._start_suit = None

    def __repr__(self) -> str:
        """ A repr string for the object."""
        cards = ', '.join([f'"{card.name}"' for card in self._cards])
        return f'Trick(cards={cards})'

    def __str__(self) -> str:
        """ A str string for the object."""
        cards = ', '.join([card.name for card in self._cards])
        text = (f'Trick: Leader: {self._leader}, winner: {self.winner}, '
                f', cards: {cards}')
        return text

    def complete(self, trump_suit: Union[Suit, None]=None):
        """Complete the trick fields."""
        if len(self._cards) != 4:
            raise ValueError(f'Trick contains {len(self._cards)} card(s)')
        suit = self._cards[0].suit
        max_value = -1
        leader = SEATS.index(self._leader)
        winner_seat = 0
        for index, card in enumerate(self._cards):
            value = card.value
            if card.suit != suit:
                if trump_suit:
                    if card.suit == trump_suit:
                        value += 13
                    else:
                        value = 0
                else:
                    value = 0
            if value > max_value:
                max_value = value
                winner_seat = index
        self.winner = SEATS[(leader + winner_seat) % 4]

    @property
    def cards(self) -> List[Card]:
        """Return the cards as a list."""
        return self._cards

    @cards.setter
    def cards(self, value: Union[List[Card], List[str]]):
        """Set the value of the cards list."""
        self._cards = self._card_setter(value)

    def _card_setter(self, cards: Union[List[Card], List[str]]):
        """Return the cards list."""
        if not isinstance(cards, list):
            raise TypeError('Cards not a list.')
        card_list = []
        for index, card in enumerate(cards):
            if isinstance(card, str):
                if card not in CARD_NAMES:
                    raise ValueError('Invalid card name')
                card = Card(card)
            elif not isinstance(card, Card):
                raise TypeError('Item is not a card')
            if index == 0:
                self._start_suit = card.suit
            card_list.append(card)
        return card_list


    @property
    def leader(self) -> str:
        """Return  seat of the leader as a string."""
        return self._leader

    @leader.setter
    def leader(self, value: str):
        """Set the value of the leader as a string."""
        if value:
            if not isinstance(value, str):
                raise TypeError('Leader must be a string')
            if value not in SEATS:
                raise ValueError('Invalid seat')
            self._leader = value

    @property
    def start_suit(self) -> Union[Suit, None]:
        """Return the Suit of the lead card in the trick."""
        if not self._start_suit and self._cards:
            self._start_suit = self.cards[0].suit
        return self._start_suit

    @property
    def suit(self) -> Union[Suit, None]:
        """Return the Suit of the lead card in the trick."""
        if not self._start_suit and self._cards:
            self._start_suit = self.cards[0].suit
        return self._start_suit

    def to_json(self):
        """Return a json representation of the class."""
        context = {
            'cards': [card.name for card in self.cards],
            'leader': self.leader,
            'note_keys': self.note_keys,
            'winner': self.winner,
        }
        return json.dumps(context)

    def from_json(self, json_str):
        """Construct and return the class from json input."""
        context = json.loads(json_str)
        self.cards = [Card(name) for name in context['cards']]
        self.leader = context['leader']
        self.winner = context['winner']
        return self