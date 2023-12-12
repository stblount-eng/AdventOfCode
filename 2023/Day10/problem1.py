from pathlib import Path

test_path1 = Path.cwd()/'Day10'/'d10p1testdata1.txt'
test_path2 = Path.cwd()/'Day10'/'d10p1testdata2.txt'
path = Path.cwd()/'Day10'/'d10p1data.txt'

def move(direction):
    match direction:
        case 'N':
            return [0, -1]
        case 'E':
            return [1, 0]
        case 'S':
            return [0, 1]
        case 'W':
            return [-1, 0]

def get_opposite(entry):
    match entry:
        case 'N':
            return 'S'
        case 'E':
            return 'W'
        case 'S':
            return 'N'
        case 'W':
            return 'E'

def pipe_exit(pipe, entry):
    match pipe:
        case '|':
            if entry == 'N':
                return 'S'
            return 'N'
        case '-':
            if entry == 'E':
                return 'W'
            return 'E'
        case 'L':
            if entry == 'N':
                return 'E'
            return 'N'
        case 'J':
            if entry == 'N':
                return 'W'
            return 'N'
        case '7':
            if entry == 'S':
                return 'W'
            return 'S'
        case 'F':
            if entry == 'S':
                return 'E'
            return 'S'

def max_distance(path):
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
    if S_adj[0] in ['|', '7', 'F']:
        y -= 1
        entry = 'S'
    elif S_adj[1] in ['-', 'J', '7']:
        x += 1
        entry = 'W'
    elif S_adj[2] in ['|', 'L', 'J']:
        y += 1
        entry = 'N'
    elif S_adj[3] in ['-', 'F', 'L']:
        x -= 1
        entry = 'E'
    total_steps = 1
    while pipe_map[y][x] != 'S':
        exit = pipe_exit(pipe_map[y][x], entry)
        x, y = x + move(exit)[0], y + move(exit)[1]
        entry = get_opposite(exit)
        total_steps += 1

    return int(total_steps/2)

assert max_distance(test_path1) == 4
assert max_distance(test_path2) == 8
print(max_distance(path))