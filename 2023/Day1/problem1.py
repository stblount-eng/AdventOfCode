from pathlib import Path

def first_and_last(line: str) -> int:
    left = ''
    right = ''
    for char in line:
        if char.isnumeric() and left == '':
            left = char
        elif char.isnumeric():
            right = char
        
    if right == '':
        return int(left + left)
    return int(left + right)

path = Path.cwd()/'Day1'/'d1p1testdata.txt'
with path.open() as test_data:
    total = 0
    for line in test_data:
        total += first_and_last(line)
assert total == 142

path = Path.cwd()/'Day1'/'d1p1data.txt'
with path.open() as test_data:
    total = 0
    for line in test_data:
        total += first_and_last(line)
print(total)