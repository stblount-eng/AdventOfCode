from pathlib import Path
import math

test_path = Path.cwd()/'Day6'/'d6p1testdata.txt'
path = Path.cwd()/'Day6'/'d6p1data.txt'

def margin(path):
    with path.open() as data:
        times = data.readline().strip().split(' ')[1:]
        distances = data.readline().strip().split(' ')[1:]
        times = [int(time) for time in times if time != '']
        distances = [int(d) for d in distances if d != '']
    ways_to_win = []
    for i in range(len(times)):
        test_time = 0
        wins = 0
        while test_time < times[i]:
            speed = test_time
            test_dist = (times[i] - test_time) * speed
            if test_dist > distances[i]:
                wins += 1
            test_time += 1
        ways_to_win.append(wins)
    return math.prod(ways_to_win)

assert margin(test_path) == 288
print(margin(path))