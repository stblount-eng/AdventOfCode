from pathlib import Path
import re

test_path = Path.cwd()/'Day4'/'d4p1testdata.txt'
path = Path.cwd()/'Day4'/'d4p1data.txt'


def total_points(path):
    with path.open() as data:
        points = 0
        for card in data:
            card = re.sub(r'(Card[ 0-9]*:)', '', card).strip()
            card = card.split('|')
            winners = card[0]
            numbers = card[1]
            winners = [winner for winner in winners.split(' ') if winner != '']
            numbers = [number for number in numbers.split(' ') if number != '']
            card_points = 0
            for number in numbers:
                if number in winners:
                    if card_points == 0 or card_points == 1:
                        card_points += 1
                    else:
                        card_points *= 2
            points += card_points
    return points

assert total_points(test_path) == 13
print(total_points(path))