from pathlib import Path
from typing import Literal

type Springs = list[Literal['.', '#', '?']]

test_path1: Path = Path.cwd()/'Day12'/'d12p1testdata1.txt'
test_path2: Path = Path.cwd()/'Day12'/'d12p1testdata2.txt'
test_path3: Path = Path.cwd()/'Day12'/'d12p1testdata3.txt'
test_path4: Path = Path.cwd()/'Day12'/'d12p1testdata4.txt'
test_path5: Path = Path.cwd()/'Day12'/'d12p1testdata5.txt'
test_path6: Path = Path.cwd()/'Day12'/'d12p1testdata6.txt'
path = Path.cwd()/'Day12'/'d12p1data.txt'

def handle_dot(line: Springs, group: list[int], cur_group: int):
    if cur_group == 0:
        return test_line(line, group, cur_group)
    if group == []:
        return 0
    group_val: int = group.pop()
    if cur_group == group_val:
        return test_line(line, group, 0)
    return 0

def test_line(line: Springs, group: list[int], cur_group: int) -> int:
    if line == []:
        if group == []:
            return 1
        return 0
    char = line.pop()
    if char == '.':
        return handle_dot(line, group, cur_group)
    if char == '#':
        if group == []:
            return 0
        cur_group += 1
        return test_line(line, group, cur_group)
    is_spring = test_line(line, group, cur_group + 1)
    not_spring = handle_dot(line, group, cur_group)
    return is_spring + not_spring

def arrangements(path: Path) -> int:
    total: int = 0
    with path.open() as data:
        for line in data:
            springs: Springs = [spring for spring in line.split(' ')[0]]
            spring_group: list[int] = [int(sc) for sc in line.split(' ')[1].split(',')]
            total += test_line(springs, spring_group, 0)
    return total

print(arrangements(test_path1) == 1 )
print(arrangements(test_path2) == 4 )
print(arrangements(test_path3) == 1 )
print(arrangements(test_path4) == 1 )
print(arrangements(test_path5) == 4 )
print(arrangements(test_path6) == 10)
assert arrangements(test_path1) == 1
assert arrangements(test_path2) == 4
assert arrangements(test_path3) == 1
assert arrangements(test_path4) == 1
assert arrangements(test_path5) == 4
assert arrangements(test_path6) == 10
print(arrangements(path))