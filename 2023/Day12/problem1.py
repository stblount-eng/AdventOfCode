from pathlib import Path

type Galaxy = list[list[str]]

test_path1 = Path.cwd()/'Day12'/'d12p1testdata1.txt'
test_path2 = Path.cwd()/'Day12'/'d12p1testdata2.txt'
test_path3 = Path.cwd()/'Day12'/'d12p1testdata3.txt'
test_path4 = Path.cwd()/'Day12'/'d12p1testdata4.txt'
test_path5 = Path.cwd()/'Day12'/'d12p1testdata5.txt'
test_path6 = Path.cwd()/'Day12'/'d12p1testdata6.txt'
path = Path.cwd()/'Day12'/'d12p1data.txt'

def arrangements(path: object) -> int:
    possible_arrangements: int = 0
    with path.open() as data:
        lines: list[str] = data.read().split('\n')
    for line in lines:
        springs_map: list[str] = [spring for spring in line.split(' ')[0]]
        spring_count: list[int] = [int(sc) for sc in line.split(' ')[1].split(',')]
    return possible_arrangements

assert arrangements(test_path1) == 1
assert arrangements(test_path2) == 4
assert arrangements(test_path3) == 1
assert arrangements(test_path4) == 1
assert arrangements(test_path5) == 4
assert arrangements(test_path6) == 10
print(arrangements(path))