from pathlib import Path

type Galaxy = list[list[str]]

test_path = Path.cwd()/'Day11'/'d11p1testdata.txt'
path = Path.cwd()/'Day11'/'d11p1data.txt'

def get_empty_row_columns(galaxy: Galaxy) -> tuple[set[int], set[int]]:
    empty_y: set = set()
    empty_x: set = set()
    for y, row in enumerate(galaxy):
        if '#' not in row:
            empty_y.add(y)
    for x in range(len(galaxy[0])):
        col: list = [row[x] for row in galaxy]
        if '#' not in col:
            empty_x.add(x)
    return empty_x, empty_y

def get_star_coord(galaxy: Galaxy) -> list[tuple[int, int]]:
    stars: list[tuple[int, int]] = []
    for y in range(len(galaxy)):
        for x in range(len(galaxy[0])):
            if galaxy[y][x] == '#':
                stars.append((x,y))
    return stars

def get_distance(star1: tuple[int, int], star2: tuple[int, int], empty_x: set[int], empty_y: set[int], mult: int) -> int:
    x_min = min(star1[0], star2[0])
    x_max = max(star1[0], star2[0])
    y_min = min(star1[1], star2[1])
    y_max = max(star1[1], star2[1])

    x_range: list[int] = [x for x in range(x_min, x_max)]
    y_range: list[int] = [y for y in range(y_min, y_max)]
    extra_x = (len([x for x in x_range if x in empty_x]))*(mult - 1)
    extra_y = (len([y for y in y_range if y in empty_y]))*(mult - 1)
    x_dist: int = abs(x_max - x_min) + extra_x
    y_dist: int = abs(y_max - y_min) + extra_y
    return x_dist + y_dist

def galaxy_distances(path: object, mult: int) -> int:
    total: int = 0
    galaxy: Galaxy = []
    with path.open() as data:
        for line in data:
            galaxy.append([char for char in line.strip()])
    empty_x, empty_y = get_empty_row_columns(galaxy)
    stars = get_star_coord(galaxy)
    while stars:
        star1: tuple[int, int] = stars.pop()
        for star2 in stars:
            total += get_distance(star1, star2, empty_x, empty_y, mult)

    return total

assert galaxy_distances(test_path, 2) == 374
assert galaxy_distances(test_path, 10) == 1030
assert galaxy_distances(test_path, 100) == 8410
print(galaxy_distances(path, 1000000))