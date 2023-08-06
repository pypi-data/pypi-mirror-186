"""The contract object for the bridgeobjects module."""

import json
from typing import List, Union

from .denomination import Denomination
from .call import Call
from .suit import Suit
from .auction import Auction
from .constants import (
    CONTRACTS, SEATS, SUITS,
    UNDER_TRICK_POINTS, UNDER_TRICK_POINTS_DOUBLED, UNDER_TRICK_POINTS_REDOUBLED,
    CONTRACT_POINTS, CONTRACT_POINTS_DOUBLED, CONTRACT_POINTS_REDOUBLED,
    OVER_TRICK_POINTS, OVER_TRICK_POINTS_DOUBLED, OVER_TRICK_POINTS_REDOUBLED,
    PART_GAME_BONUS, GAME_BONUS,
    CONTRACT_THRESHOLD, DOUBLED_BONUS, REDOUBLED_BONUS,
    SLAM_LEVEL, GRAND_SLAM_LEVEL,
    SLAM_BONUS, GRAND_SLAM_BONUS
    )

__all__ = ['Contract']


class Contract(object):
    """
    A Contract object for the bridgeobjects module.

    A contract has a declarer, a denomination.

    Parameters
    ----------
    name: (str) call's name
    declarer: (str) the declarer's seat name

    Example
    -------
        contract = Contract("3NTX", "S")

    It is also identified (if appropriate) as either major, minor or no trumps.
    """

    def __init__(self, name: str = '', declarer: str = '', auction: Union[Auction, None] = None):
        self._initialise(name, declarer, auction)

    def _initialise(self, name, declarer, auction=None):
        """Initialise the class."""
        (self._name, self._modifier) = self._get_name(name)
        self._declarer = declarer
        self.auction = self._analyse_auction(auction)
        self._is_nt = False
        self._denomination = None

        # Denomination
        if self._name and self._is_valid(self._name):
            self._call = Call(self._name)
            self._denomination = self._get_denomination(self._name)
            if self._denomination:
                self._is_nt = self._denomination.is_nt
            if self._is_nt:
                self._trump_suit = None
            else:
                self._trump_suit = self._denomination.name
        else:
            self._trump_suit = None
            self._call = Call('')

        # Level
        if self._name:
            self._level = int(self._name[0])
            self._target_tricks = self._level + CONTRACT_THRESHOLD
            self.game_level = self._is_game_level()
        else:
            self._level = 0
            self._target_tricks = 0
            self.game_level = False

        # Modifier
        self._set_double()

    def __repr__(self) -> str:
        """Return the repr string for the object."""
        return f'Contract("{self._call.name}", "{self._declarer}")'

    def __str__(self) -> str:
        """Return the str string for the object."""
        return f'Contract. {self._call.name} by {self._declarer}'

    def _is_game_level(self):
        """Return True if the  contract is at or above game level."""
        if self.denomination.is_minor:
            if self.level >= 5:
                return True
        elif self.denomination.is_major:
            if self.level >= 4:
                return True
        else:
            if self.level >= 3:
                return True
        return False

    @staticmethod
    def _get_name(name):
        """Return the name and modifier from the name parameter."""
        if name and name != 'None':
            if len(name) >= 3 and name[-1] in 'DR':
                return (name[:-1], name[-1])
            return (name, '')
        return ('', '')

    def _set_double(self):
        """Set the value of the doubled for the contract."""
        self.redoubled = False
        self.doubled = False
        if self._modifier == 'R':
            self.redoubled = True
        elif self._modifier == 'D':
            self.doubled = True

    @property
    def declarer(self) -> str:
        """Return the declarer value."""
        return self._declarer

    @declarer.setter
    def declarer(self, value: str):
        """Assign the declarer value."""
        if value and value not in SEATS:
            raise ValueError(f"'{value}' is not a valid seat")
        self._declarer = value

    @property
    def leader(self) -> Union[str, None]:
        """Return the dealer value."""
        if self._declarer:
            return SEATS[(SEATS.index(self._declarer) + 1) % 4]
        return None

    @property
    def name(self) -> str:
        """Return the name value."""
        return f'{self._name}{self.modifier}'

    @name.setter
    def name(self, value: str):
        """Assign the name value."""
        if not value:
            return
        if self._is_valid(value):
            self._denomination = self._get_denomination(value)
            self._is_nt = self._denomination.is_nt
            if not self._is_nt:
                self._trump_suit = SUITS[value[1]]
        (self._name, self._modifier) = self._get_name(value)
        self._level = int(self._name[0])
        self._target_tricks = self._level + CONTRACT_THRESHOLD
        self._call = Call(self._name)

    @property
    def call(self) -> Call:
        """Return the call value."""
        return self._call

    @call.setter
    def call(self, value: Union[str, Call]):
        """Assign the denomination value."""
        if isinstance(value, str):
            if value in CONTRACTS:
                value = Call(value)
            else:
                raise ValueError(f'{value} is not a valid Call')
        elif not isinstance(value, Call):
            raise TypeError(f'{value} is not a Call')
        self._call = value
        self._denomination = self._get_denomination(value.name)
        self._is_nt = self._denomination.is_nt or self._denomination.is_no_trumps

    @property
    def trump_suit(self) -> Union[Suit, None]:
        """Return a value for the trump suit as a Suit."""
        return self._trump_suit

    @trump_suit.setter
    def trump_suit(self, value: Union[str, Suit]):
        """Set the value of the trump suit as a Suit."""
        if isinstance(value, str) and value in SUITS:
            value = SUITS[value]
        elif not isinstance(value, Suit):
            raise TypeError(f'{value} is not a suit.')
        self._denomination = Denomination(value.name)
        self._trump_suit = value

    @property
    def level(self) -> int:
        """Return the level value."""
        return self._level

    @property
    def denomination(self) -> Union[Denomination, None]:
        """Return the denomination value."""
        return self._denomination

    @property
    def is_nt(self) -> bool:
        """Return True if the denomination is NT."""
        return self._is_nt

    @property
    def modifier(self) -> str:
        """Return contract's modifier (i.e.: '', 'D' or 'R')."""
        return self._modifier

    @modifier.setter
    def modifier(self, value: str):
        """Set contract's modifier (i.e.: '', 'D' or 'R')."""
        if value in ['D', 'R']:
            self._modifier = value
        else:
            self._modifier = ''

    @property
    def target_tricks(self) -> int:
        """Return the number of tricks needed to make the contract."""
        return self._target_tricks

    @staticmethod
    def _is_valid(name: str) -> bool:
        """Return True if the contact name is valid."""
        if not name:
            return True
        if len(name) >= 3 and name[-1] in 'DR':
            name = name[:-1]
        if name not in CONTRACTS:
            raise ValueError(f'{name} is not a valid contract')
        return True

    @staticmethod
    def _get_denomination(name: str) -> Denomination:
        """Return the denomination of the contract."""
        if not name:
            return ''
        if name[1:3] == 'NT':
            return Denomination('NT')
        return Denomination(name[1])

    def _analyse_auction(self, auction: Union[Auction, None]) -> Union[Auction, None]:
        """Generate name and declarer from auction and return auction."""
        if auction:
            if auction.calls and auction.first_caller:
                if (self._three_final_passes(auction.calls) and
                        not self._passed_out(auction.calls)):
                    dealer_index = SEATS.index(auction.first_caller)

                    auction_calls = [call for call in auction.calls]
                    auction_calls.reverse()
                    for call in auction_calls:
                        if call.is_value_call:
                            break

                    denomination = call.denomination
                    for index, check_call in enumerate(auction.calls):
                        if check_call.denomination == denomination:
                            break
                    declarer_index = (dealer_index + index) % 4
                    self._declarer = SEATS[declarer_index]
                    self._name = call.name
                    return auction
        return None

    @staticmethod
    def _three_final_passes(calls: List[Call]) -> bool:
        """Return True if there have been three consecutive passes."""
        three_passes = False
        if len(calls) >= 4:
            if calls[-1].is_pass and calls[-2].is_pass and calls[-3].is_pass:
                three_passes = True
        return three_passes

    @staticmethod
    def _passed_out(calls: List[Call]) -> bool:
        """Return True if the board has been passed out."""
        if len(calls) != 4:
            return False
        for call in calls:
            if not call.is_pass:
                return False
        return True

    def score(self, declarer_tricks: int, vulnerable: bool = False) -> int:
        """Return the score for a contract."""
        # Based on https://en.wikipedia.org/wiki/Bridge_scoring#Contract_points

        contract_made = self.level + CONTRACT_THRESHOLD <= declarer_tricks
        if contract_made:
            return self._contract_made(declarer_tricks, vulnerable)
        else:
            return self._contract_failed(declarer_tricks, vulnerable)

    def _contract_made(self, declarer_tricks: int, vulnerable: bool) -> int:
        """Return the score if the contract is made."""
        score = 0
        contract_points = self._contract_points()
        score += contract_points
        score += self._doubled_bonus()
        score += self._game_bonus(vulnerable, contract_points)
        score += self._overtrick_points(declarer_tricks, vulnerable)
        score += self._slam_points(vulnerable)
        return score

    def _contract_points(self) -> int:
        """Return the points earned for each trick in a made contract."""
        score = 0
        name = self.denomination.name

        if self.doubled:
            contract_points = CONTRACT_POINTS_DOUBLED[name]
        elif self.redoubled:
            contract_points = CONTRACT_POINTS_REDOUBLED[name]
        else:
            contract_points = CONTRACT_POINTS[name]

        for trick in range(self.level):
            if trick < len(contract_points):
                score += contract_points[trick]
            else:
                score += contract_points[-1]
        return score

    def _doubled_bonus(self) -> int:
        """Return the points earned for each trick in a made contract."""
        if self.doubled:
            return DOUBLED_BONUS
        elif self.redoubled:
            return REDOUBLED_BONUS
        return 0

    def _game_bonus(self, vulnerable: bool, contract_points: int) -> int:
        """Return the points earned for the game in a made contract."""
        if vulnerable:
            game_bonus = GAME_BONUS['vulnerable']
        else:
            game_bonus = GAME_BONUS['non-vulnerable']
        if contract_points > 100 or self.game_level:
            return game_bonus
        return PART_GAME_BONUS

    def _overtrick_points(self, declarer_tricks: int, vulnerable: bool) -> int:
        """Return the points earned for the overtricks."""
        score = 0
        name = self.denomination.name

        if self.doubled:
            if vulnerable:
                overtrick_points = OVER_TRICK_POINTS_DOUBLED['vulnerable']
            else:
                overtrick_points = OVER_TRICK_POINTS_DOUBLED['non-vulnerable']
        elif self.redoubled:
            if vulnerable:
                overtrick_points = OVER_TRICK_POINTS_REDOUBLED['vulnerable']
            else:
                overtrick_points = OVER_TRICK_POINTS_REDOUBLED['non-vulnerable']
        else:
            overtrick_points = OVER_TRICK_POINTS[name]

        if True:
            for trick in range(declarer_tricks - CONTRACT_THRESHOLD - self.level):
                score += overtrick_points
        return score

    def _slam_points(self, vulnerable: bool) -> int:
        """Return the points earned for a slam."""
        if self.level == SLAM_LEVEL:
            if vulnerable:
                return SLAM_BONUS['vulnerable']
            else:
                return SLAM_BONUS['non-vulnerable']
        if self.level == GRAND_SLAM_LEVEL:
            if vulnerable:
                return GRAND_SLAM_BONUS['vulnerable']
            else:
                return GRAND_SLAM_BONUS['non-vulnerable']
        return 0

    def _contract_failed(self, declarer_tricks: int, vulnerable: bool):
        score = 0
        undertricks = self._target_tricks - declarer_tricks
        if self.doubled:
            regime = UNDER_TRICK_POINTS_DOUBLED
        elif self.redoubled:
            regime = UNDER_TRICK_POINTS_REDOUBLED
        else:
            regime = UNDER_TRICK_POINTS
        if vulnerable:
            points = regime['vulnerable']
        else:
            points = regime['non-vulnerable']
        for trick in range(undertricks):
            if trick > len(points)-1:
                score -= points[-1]
            else:
                score -= points[trick]
        return score

    def to_json(self):
        """Return a json representation of the class."""
        context = {
            'name': f'{self._call.name}{self._modifier}',
            'declarer': self._declarer,
        }
        return json.dumps(context)

    def from_json(self, json_str):
        """Construct and return the class from json input."""
        name, declarer = '', ''
        context = json.loads(json_str)
        if 'name' in context:
            name = context['name']
            if name == 'None':
                name = None
        if 'declarer' in context:
            declarer = context['declarer']
        self._initialise(name, declarer)
        return self