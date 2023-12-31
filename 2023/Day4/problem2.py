from pathlib import Path
import re

test_path = Path.cwd()/'2023'/'Day4'/'d4p1testdata.txt'
path = Path.cwd()/'2023'/'Day4'/'d4p1data.txt'

def process_card(card):
    card = re.sub(r'(Card[ 0-9]*:)', '', card).strip()
    card = card.split('|')
    winners = card[0]
    numbers = card[1]
    winners = [winner for winner in winners.split(' ') if winner != '']
    numbers = [number for number in numbers.split(' ') if number != '']
    return winners, numbers


def total_points(path):
    with path.open() as data:
        points = 0
        for card in data:
            winners, numbers = process_card(card)
            card_points = 0
            for number in numbers:
                if number in winners:
                    if card_points == 0 or card_points == 1:
                        card_points += 1
                    else:
                        card_points *= 2
            points += card_points
    return points

# assert total_points(test_path) == 13
# print(total_points(path))

def total_cards(path):
    with path.open() as data:
        card_total = 0
        card_repeats = {}
        for current_card, card in enumerate(data):
            if current_card not in card_repeats:
                card_repeats[current_card] = 0
            card_repeats[current_card] += 1
            winners, numbers = process_card(card)
            card_points = 0
            for number in numbers:
                if number in winners:
                    card_points += 1
            for card_to_dup in range(current_card + 1, current_card + card_points + 1):
                if card_to_dup not in card_repeats:
                    card_repeats[card_to_dup] = card_repeats[current_card]
                else:
                    card_repeats[card_to_dup] += card_repeats[current_card]
    return sum(card_repeats.values())

assert total_cards(test_path) == 30
print(total_cards(path))