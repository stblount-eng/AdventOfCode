from pathlib import Path
from collections import Counter

test_path1 = Path.cwd()/'Day10'/'d10p1testdata1.txt'
test_path2 = Path.cwd()/'Day10'/'d10p1testdata2.txt'
path = Path.cwd()/'Day10'/'d10p1data.txt'

def next_pipe(adj_pipes, current_dir):
    pipe_opt = {
        '|': ['N','S'],
        '-': ['E','W'],
        'L': ['N','E'],
        'J': ['N','W'],
        '7': ['S','W'],
        'F': ['S','E'],
    }


def max_distance(path):
    max_distance = 0
    with path.open() as data:
        pipe_map = []
        for j, line in enumerate(data):
            pipe_line = []
            for i, char in enumerate(line.strip()):
                pipe_line.append(char)
                if char == 'S':
                    x = i
                    y = j
            pipe_map.append(pipe_line)
        S_adj = [pipe_map[y-1][x], pipe_map[y][x+1], pipe_map[y+1][x], pipe_map[y][x-1]]

    return max_distance

assert max_distance(test_path1) == 4
assert max_distance(test_path2) == 8
print(max_distance(path))