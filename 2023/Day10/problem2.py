from pathlib import Path
from typing import Literal

type Compass = Literal['S', 'N', 'W', 'E']
type Pipe = Literal['|', '-', 'L', 'J', '7', 'F']
type NotPipe = Literal['.', 'S']
type PipeMap = list[list[Pipe | NotPipe]]
type PipeRoute = list[tuple[int, int]]

test_path1 = Path.cwd()/'2023'/'Day10'/'d10p1testdata1.txt'
test_path2 = Path.cwd()/'2023'/'Day10'/'d10p1testdata2.txt'
test_path3 = Path.cwd()/'2023'/'Day10'/'d10p2testdata1.txt'
test_path4 = Path.cwd()/'2023'/'Day10'/'d10p2testdata2.txt'
path = Path.cwd()/'2023'/'Day10'/'d10p1data.txt'

def move(direction: Compass) -> list[int]:
    match direction:
        case 'N':
            return [0, -1]
        case 'E':
            return [1, 0]
        case 'S':
            return [0, 1]
        case 'W':
            return [-1, 0]

def get_opposite(entry: Compass) -> Compass:
    match entry:
        case 'N':
            return 'S'
        case 'E':
            return 'W'
        case 'S':
            return 'N'
        case 'W':
            return 'E'

def pipe_exit(pipe: Pipe, entry: Compass) -> Compass:
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

def create_pipe_map(path: object) -> tuple[PipeMap, tuple[int, int]]:
    with path.open() as data:
        pipe_map = []
        x: int = 0
        y: int = 0
        for j, line in enumerate(data):
            pipe_line = []
            for i, char in enumerate(line.strip()):
                pipe_line.append(char)
                if char == 'S':
                    x = i
                    y = j
            pipe_map.append(pipe_line)
    return pipe_map, (x,y)

def create_pipe_route(pipe_map: PipeMap, start: tuple[int, int]) -> PipeRoute:
    x: int = start[0]
    y: int = start[1]
    S_adj = [pipe_map[y-1][x], pipe_map[y][x+1], pipe_map[y+1][x], pipe_map[y][x-1]]
    if S_adj[0] in ['|', '7', 'F']:
        y -= 1
        entry: str = 'S'
    elif S_adj[1] in ['-', 'J', '7']:
        x += 1
        entry: str = 'W'
    elif S_adj[2] in ['|', 'L', 'J']:
        y += 1
        entry: str = 'N'
    else:
        x -= 1
        entry: str = 'E'
    pipe_route = [(x,y)]
    while pipe_map[y][x] != 'S':
        exit: Compass = pipe_exit(pipe_map[y][x], entry)
        x, y = x + move(exit)[0], y + move(exit)[1]
        entry = get_opposite(exit)
        pipe_route.append((x,y))
    return pipe_route

def max_distance(path: object) -> int:
    pipemap, start = create_pipe_map(path)
    pipe_route = create_pipe_route(pipemap, start)
    return int(len(pipe_route)/2)

def is_enclosed(posx: int, posy: int) -> bool:
    return True

def num_tiles(path: object) -> int:
    pipemap, start = create_pipe_map(path)
    pipe_route = create_pipe_route(pipemap, start)
    inner_tiles = polygonArea(pipe_route) - (len(pipe_route)/2) + 1
    return int(inner_tiles)

def polygonArea(vertices: PipeRoute) -> int:
  numberOfVertices = len(vertices)
  sum1 = 0
  sum2 = 0
  
  for i in range(0,numberOfVertices-1):
    sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
    sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]
  
  sum1 = sum1 + vertices[numberOfVertices-1][0]*vertices[0][1]   
  sum2 = sum2 + vertices[0][0]*vertices[numberOfVertices-1][1]   
  
  area = abs(sum1 - sum2) / 2
  return int(area)

assert max_distance(test_path1) == 4
assert max_distance(test_path2) == 8
assert num_tiles(test_path3) == 4
assert num_tiles(test_path4) == 10
print(max_distance(path))
print(num_tiles(path))