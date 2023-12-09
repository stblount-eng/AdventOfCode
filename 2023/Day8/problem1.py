from pathlib import Path
from collections import Counter

test_path = Path.cwd()/'Day7'/'d7p1testdata.txt'
path = Path.cwd()/'Day7'/'d7p1data.txt'

def get_hand_type(hand: str) -> str:
    card_count = Counter(hand)
    top_cards = card_count.most_common(2)
    match top_cards[0][1]:
        case 5:
            return '7'
        case 4:
            return '6'
        case 3:
            if top_cards[1][1] == 2:
                return '5'
            return '4'
        case 2:
            if top_cards[1][1] == 2:
                return '3'
            return '2'
    return '1'

def get_hand_value(hand):
    value = ''
    value += get_hand_type(hand)
    for char in hand:
        if char.isalpha():
            match char:
                case 'A':
                    value += '14'
                case 'K':
                    value += '13'
                case 'Q':
                    value += '12'
                case 'J':
                    value += '11'
                case 'T':
                    value += '10'
        else:
            value += '0' + char
    return int(value)

def total_winnings(path):
    with path.open() as data:
        hands = data.read().split('\n')
    hands = [hand.split(' ') for hand in hands]
    winnings = 0
    for hand in hands:
        hand.append(get_hand_value(hand[0]))
    hands_sorted = sorted(hands, key=lambda hand: hand[2])
    for i, hand in enumerate(hands_sorted):
        winnings += (i + 1) * int(hand[1])
    return winnings

assert total_winnings(test_path) == 6440
print(total_winnings(path))