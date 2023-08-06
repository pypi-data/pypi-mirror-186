"""A set of tests for the bridgeobjects Trick class."""
import pytest

from ..source.contract import Contract

vulnerable_text = {
    True: 'vulnerable',
    False: 'non-vulnerable',
}
doubled_text = {
    '': 'not doubled',
    'D': 'doubled',
    'R': 'redoubled',
}

undertrick_scores = {
    'non-vulnerable, not doubled': [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650],
    'non-vulnerable, doubled': [100, 300, 500, 800, 1100, 1400, 1700, 2000, 2300, 2600, 2900, 3200, 3500],
    'non-vulnerable, redoubled': [200, 600, 1000, 1600, 2200, 2800, 3400, 4000, 4600, 5200, 5800, 6400, 7000],
    'vulnerable, not doubled': [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300],
    'vulnerable, doubled': [200, 500, 800, 1100, 1400, 1700, 2000, 2300, 2600, 2900, 3200, 3500, 3800],
    'vulnerable, redoubled': [400, 1000, 1600, 2200, 2800, 3400, 4000, 4600, 5200, 5800, 6400, 7000, 7600],
}

scores_one_minor = {
    'non-vulnerable, not doubled': [70, 90, 110, 130, 150, 170, 190],
    'non-vulnerable, doubled': [140, 240, 340, 440, 540, 640, 740],
    'non-vulnerable, redoubled': [230, 430, 630, 830, 1030, 1230, 1430],
    'vulnerable, not doubled': [70, 90, 110, 130, 150, 170, 190],
    'vulnerable, doubled': [140, 340, 540, 740, 940, 1140, 1340],
    'vulnerable, redoubled': [230, 630, 1030, 1430, 1830, 2230, 2630],
}

scores_two_minor = {
    'non-vulnerable, not doubled': [90, 110, 130, 150, 170, 190],
    'non-vulnerable, doubled': [180, 280, 380, 480, 580, 680],
    'non-vulnerable, redoubled': [560, 760, 960, 1160, 1360, 1560]
,
    'vulnerable, not doubled': [90, 110, 130, 150, 170, 190],
    'vulnerable, doubled': [180, 380, 580, 780, 980, 1180],
    'vulnerable, redoubled': [760, 1160, 1560, 1960, 2360, 2760],
}

scores_three_minor = {
    'non-vulnerable, not doubled': [110, 130, 150, 170, 190],
    'non-vulnerable, doubled': [470, 570, 670, 770, 870],
    'non-vulnerable, redoubled': [640, 840, 1040, 1240, 1440],
    'vulnerable, not doubled': [110, 130, 150, 170, 190],
    'vulnerable, doubled': [670, 870, 1070, 1270, 1470],
    'vulnerable, redoubled': [840, 1240, 1640, 2040, 2440],
}

scores_four_minor = {
    'non-vulnerable, not doubled': [130, 150, 170, 190],
    'non-vulnerable, doubled': [510, 610, 710, 810],
    'non-vulnerable, redoubled': [720, 920, 1120, 1320],
    'vulnerable, not doubled': [130, 150, 170, 190],
    'vulnerable, doubled': [710, 910, 1110, 1310],
    'vulnerable, redoubled': [920, 1320, 1720, 2120],
}

scores_one_major = {
    'non-vulnerable, not doubled': [80, 110, 140, 170, 200, 230, 260],
    'non-vulnerable, doubled': [160, 260, 360, 460, 560, 660, 760],
    'non-vulnerable, redoubled': [520, 720, 920, 1120, 1320, 1520, 1720],
    'vulnerable, not doubled': [80, 110, 140, 170, 200, 230, 260],
    'vulnerable, doubled': [160, 360, 560, 760, 960, 1160, 1360],
    'vulnerable, redoubled': [720, 1120, 1520, 1920, 2320, 2720, 3120],
}

scores_two_major = {
    'non-vulnerable, not doubled': [110, 140, 170, 200, 230, 260],
    'non-vulnerable, doubled': [470, 570, 670, 770, 870, 970],
    'non-vulnerable, redoubled': [640, 840, 1040, 1240, 1440, 1640],
    'vulnerable, not doubled': [110, 140, 170, 200, 230, 260],
    'vulnerable, doubled': [670, 870, 1070, 1270, 1470, 1670],
    'vulnerable, redoubled': [840, 1240, 1640, 2040, 2440, 2840],
}

scores_three_major = {
    'non-vulnerable, not doubled': [140, 170, 200, 230, 260],
    'non-vulnerable, doubled': [530, 630, 730, 830, 930],
    'non-vulnerable, redoubled': [760, 960, 1160, 1360, 1560],
    'vulnerable, not doubled': [140, 170, 200, 230, 260],
    'vulnerable, doubled': [730, 930, 1130, 1330, 1530],
    'vulnerable, redoubled': [960, 1360, 1760, 2160, 2560],
}

scores_one_nt = {
    'non-vulnerable, not doubled': [90, 120, 150, 180, 210, 240, 270],
    'non-vulnerable, doubled': [180, 280, 380, 480, 580, 680, 780],
    'non-vulnerable, redoubled': [560, 760, 960, 1160, 1360, 1560, 1760],
    'vulnerable, not doubled': [90, 120, 150, 180, 210, 240, 270],
    'vulnerable, doubled': [180, 380, 580, 780, 980, 1180, 1380],
    'vulnerable, redoubled': [760, 1160, 1560, 1960, 2360, 2760, 3160],
}

scores_two_nt = {
    'non-vulnerable, not doubled': [120, 150, 180, 210, 240, 270],
    'non-vulnerable, doubled': [490, 590, 690, 790, 890, 990],
    'non-vulnerable, redoubled': [680, 880, 1080, 1280, 1480, 1680],
    'vulnerable, not doubled': [120, 150, 180, 210, 240, 270],
    'vulnerable, doubled': [690, 890, 1090, 1290, 1490, 1690],
    'vulnerable, redoubled': [880, 1280, 1680, 2080, 2480, 2880],
}

scores_five_minor = {
    'non-vulnerable, not doubled': [400, 420, 440],
    'non-vulnerable, doubled': [550, 650, 750],
    'non-vulnerable, redoubled': [800, 1000, 1200],
    'vulnerable, not doubled': [600, 620, 640],
    'vulnerable, doubled': [750, 950, 1150],
    'vulnerable, redoubled': [1000, 1400, 1800],
}

scores_four_major = {
    'non-vulnerable, not doubled': [420, 450, 480, 510],
    'non-vulnerable, doubled': [590, 690, 790, 890],
    'non-vulnerable, redoubled': [880, 1080, 1280, 1480],
    'vulnerable, not doubled': [620, 650, 680, 710],
    'vulnerable, doubled': [790, 990, 1190, 1390],
    'vulnerable, redoubled': [1080, 1480, 1880, 2280],
}

scores_three_nt = {
    'non-vulnerable, not doubled': [400, 430, 460, 490, 520],
    'non-vulnerable, doubled': [550, 650, 750, 850, 950],
    'non-vulnerable, redoubled': [800, 1000, 1200, 1400, 1600],
    'vulnerable, not doubled': [600, 630, 660, 690, 720],
    'vulnerable, doubled': [750, 950, 1150, 1350, 1550],
    'vulnerable, redoubled': [1000, 1400, 1800, 2200, 2600],
}

scores_six_nt = {
    'non-vulnerable, not doubled': [990, 1020],
    'non-vulnerable, doubled': [1230, 1330],
    'non-vulnerable, redoubled': [1660, 1860],
    'vulnerable, not doubled': [1440, 1470],
    'vulnerable, doubled': [1680, 1880],
    'vulnerable, redoubled': [2110, 2510],
}

scores_six_major = {
    'non-vulnerable, not doubled': [980, 1010],
    'non-vulnerable, doubled': [1210, 1310],
    'non-vulnerable, redoubled': [1620, 1820],
    'vulnerable, not doubled': [1430, 1460],
    'vulnerable, doubled': [1660, 1860],
    'vulnerable, redoubled': [2070, 2470],
}

scores_six_minor = {
    'non-vulnerable, not doubled': [920, 940],
    'non-vulnerable, doubled': [1090, 1190],
    'non-vulnerable, redoubled': [1380, 1580],
    'vulnerable, not doubled': [1370, 1390],
    'vulnerable, doubled': [1540, 1740],
    'vulnerable, redoubled': [1830, 2230],
}

scores_seven_nt = {
    'non-vulnerable, not doubled': [1520],
    'non-vulnerable, doubled': [1790],
    'non-vulnerable, redoubled': [2280],
    'vulnerable, not doubled': [2220],
    'vulnerable, doubled': [2490],
    'vulnerable, redoubled': [2980],
}

scores_seven_major = {
    'non-vulnerable, not doubled': [1510],
    'non-vulnerable, doubled': [1770],
    'non-vulnerable, redoubled': [2240],
    'vulnerable, not doubled': [2210],
    'vulnerable, doubled': [2470],
    'vulnerable, redoubled': [2940],
}

scores_seven_minor = {
    'non-vulnerable, not doubled': [1440],
    'non-vulnerable, doubled': [1630],
    'non-vulnerable, redoubled': [1960],
    'vulnerable, not doubled': [2140],
    'vulnerable, doubled': [2330],
    'vulnerable, redoubled': [2660],
}


# Undertricks

def test_undertricks():
    """Test undertricks."""
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            contract = Contract('7S'+doubled, 'N')
            scores = undertrick_scores[score_key]
            for index, declarers_tricks in enumerate(range(12, 0, -1)):
                assert contract.score(declarers_tricks, vulnerable=vulnerable) == -1 * scores[index]

# Contract made below game level - Minors


def test_one_minor():
    """Test scores for a one of a minor."""
    level = 1
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_one_minor[score_key]
            contract = Contract(f'{level}C{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_two_minor():
    """Test scores for a two of a minor."""
    level = 2
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_two_minor[score_key]
            contract = Contract(f'{level}C{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_three_minor():
    """Test scores for a three of a minor."""
    level = 3
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_three_minor[score_key]
            contract = Contract(f'{level}C{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_four_minor():
    """Test scores for a four of a minor."""
    level = 4
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_four_minor[score_key]
            contract = Contract(f'{level}C{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]

# Contract made below game level - Majors

def test_one_major():
    """Test scores for a one of a major."""
    level = 1
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_one_major[score_key]
            contract = Contract(f'{level}H{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_two_major():
    """Test scores for a two of a major."""
    level = 2
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_two_major[score_key]
            contract = Contract(f'{level}H{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_three_major():
    """Test scores for a three of a major."""
    level = 3
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_three_major[score_key]
            contract = Contract(f'{level}H{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


# Contract made below game level - NT

def test_one_nt():
    """Test scores for one nt."""
    level = 1
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_one_nt[score_key]
            contract = Contract(f'{level}NT{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_two_nt():
    """Test scores for two nt."""
    level = 2
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_two_nt[score_key]
            contract = Contract(f'{level}NT{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


# Contract at game level

def test_five_minor():
    """Test scores five minor."""
    level = 5
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_five_minor[score_key]
            contract = Contract(f'{level}D{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_four_major():
    """Test scores four major."""
    level = 4
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_four_major[score_key]
            contract = Contract(f'{level}S{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_three_nt():
    """Test scores three nt."""
    level = 3
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_three_nt[score_key]
            contract = Contract(f'{level}NT{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                # print(contract, declarers_tricks, score_key, f'{score=}', scores[index])
                assert score == scores[index]


# Slams

def test_six_nt():
    """Test scores six nt."""
    level = 6
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_six_nt[score_key]
            contract = Contract(f'{level}NT{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_six_major():
    """Test scores six major."""
    level = 6
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_six_major[score_key]
            contract = Contract(f'{level}H{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_six_minor():
    """Test scores six minor."""
    level = 6
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_six_minor[score_key]
            contract = Contract(f'{level}D{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


# Grand Slams

def test_seven_nt():
    """Test scores seven nt."""
    level = 7
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_seven_nt[score_key]
            contract = Contract(f'{level}NT{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_seven_major():
    """Test scores seven major."""
    level = 7
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_seven_major[score_key]
            contract = Contract(f'{level}H{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]


def test_seven_minor():
    """Test scores seven minor."""
    level = 7
    for vulnerable in [False, True]:
        for doubled in ['', 'D', 'R']:
            score_key = f'{vulnerable_text[vulnerable]}, {doubled_text[doubled]}'
            scores = scores_seven_minor[score_key]
            contract = Contract(f'{level}C{doubled}', 'N')
            for index, declarers_tricks in enumerate(range(6+level, 14)):
                score = contract.score(declarers_tricks, vulnerable=vulnerable)
                assert score == scores[index]