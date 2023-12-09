from pathlib import Path
import math

test_path = Path.cwd()/'Day6'/'d6p1testdata.txt'
path = Path.cwd()/'Day6'/'d6p1data.txt'

def margin(path):
    with path.open() as data:
        times = data.readline().strip().split(' ')[1:]
        distances = data.readline().strip().split(' ')[1:]
        times = [time for time in times if time != '']
        distances = [d for d in distances if d != '']
        time = int(''.join(times))
        dist = int(''.join(distances))
    max = math.ceil(math.sqrt((time**2)/4 - dist) + (time/2))
    min = math.ceil((time/2) - math.sqrt((time**2)/4 - dist))
    print(max - min)
    return max - min

assert margin(test_path) == 71503
print(margin(path))