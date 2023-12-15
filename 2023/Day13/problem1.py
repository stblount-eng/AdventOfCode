from pathlib import Path
from typing import Literal

test_path1 = Path.cwd()/'Day13'/'d13p1testdata1.txt'
test_path2 = Path.cwd()/'Day13'/'d13p1testdata2.txt'
path = Path.cwd()/'Day13'/'d13p1data.txt'

def get_x_reflection(rock_map: list[str]) -> int:
    refl_map: dict[int, set[int]] = {}
    for y, line in enumerate(rock_map):
        refl_map[y] = set()
        for i in range(1, len(line)):
            test_range = min(len(line) - i, i)
            print(line[i - test_range:i] + '   :   ' + line[i:i + test_range])
            if line[i - test_range:i] == line[i:i + test_range][::-1]:
                refl_map[y].add(i)
    return set.intersection(*refl_map.values()).pop()

def get_y_reflection(rock_map: list[str]) -> int:
    refl_map: dict[int, set[int]] = {}
    for x in range(len(rock_map[0])):
        col = [val[0] for val in rock_map]
        refl_map[x] = set()
        for i in range(1, len(col)):
            test_range = min(len(col) - i, i)
            print(col[i - test_range:i] + col[i:i + test_range])
            if col[i - test_range:i] == col[i:i + test_range][::-1]:
                refl_map[x].add(i)
    return set.intersection(*refl_map.values()).pop()


def reflections(path: Path) -> int:
    total: int = 0
    with path.open() as data:
        maps = [rock_map.split('\n') for rock_map in data.read().split('\n\n')]
    for rock_map in maps:
        # x_line = get_x_reflection(rock_map)
        y_line = get_y_reflection(rock_map)
        # total += 100*y_line + x_line

    return total

# assert reflections(test_path1) == 5
assert reflections(test_path2) == 400
print(reflections(path))