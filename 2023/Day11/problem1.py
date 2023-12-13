from pathlib import Path
from collections import Counter

test_path = Path.cwd()/'2023'/'Day11'/'d11p1testdata.txt'
path = Path.cwd()/'2023'/'Day11'/'d11p1data.txt'

def expand_galaxy(galaxy: list[list[str]]) -> list[list[str]]:
    y_galaxy: list[list] = []
    for y, row in enumerate(galaxy):
        if '#' not in row:
            y_galaxy.append(row)
        y_galaxy.append(row)
    for x in range(len(galaxy[0])):
        col: list = [row[x] for row in y_galaxy]
        if '#' not in col:
            x_galaxy: list[list[str]] = []
            for y in range(len(y_galaxy)):
                x_galaxy.append(y_galaxy[y][:x] + ['.'] + y_galaxy[y][:x])
            y_galaxy = x_galaxy

    return new_galaxy

def galaxy_distances(path: object) -> int:
    total: int = 0
    galaxy: list[list[str]] = []
    with path.open() as data:
        for line in data:
            galaxy.append([char for char in line.strip()])
    galaxy = expand_galaxy(galaxy)

    return total

assert galaxy_distances(test_path) == 374
print(galaxy_distances(path))