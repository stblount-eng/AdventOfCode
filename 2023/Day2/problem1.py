from pathlib import Path
import re

def is_possible(game):
        balls = {
            'red': 0,
            'blue': 0,
            'green': 0
        }
        game = re.sub(r'(Game [0-9]*:)', '', game).strip()
        hands = game.split('; ')
        for hand in hands:
            hand = hand.split(', ')
            for colour in hand:
                m = re.match(r'([0-9]*) ([A-z]*)', colour)
                if balls[m.group(2)] < int(m.group(1)):
                    balls[m.group(2)] = int(m.group(1))
        if balls['red'] <= 12 and balls['green'] <= 13 and balls['blue'] <= 14:
            return True
        return False

path = Path.cwd()/'2023'/'Day2'/'d2p1testdata.txt'
with path.open() as test_data:
    total = 0
    for i, game in enumerate(test_data):
        if is_possible(game):
            total += i
            print(i)

assert total == 8

# path = Path.cwd()/'2023'/'Day2'/'d1p1data.txt'
# with path.open() as test_data:
#     total = 0
# print(total)