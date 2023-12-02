from pathlib import Path
from math import prod
import re

def cubed_balls(game):
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
    return prod([x for x in balls.values()])

path = Path.cwd()/'Day2'/'d2p1testdata.txt'
with path.open() as test_data:
    total = 0
    for game in test_data:
        total += cubed_balls(game)
        

assert total == 2286

path = Path.cwd()/'Day2'/'d2p1data.txt'
with path.open() as test_data:
    total = 0
    for game in test_data:
        total += cubed_balls(game)
print(total)