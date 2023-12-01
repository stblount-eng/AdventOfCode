from pathlib import Path

def first_and_last_string(line: str) -> int:
    left = ''
    right = ''
    valid_numbers = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for i in range(len(line)):
        three_letter = four_letter = five_letter = number = ''
        max_length = len(line) - i
        if max_length > 2:
            three_letter = line[i:i + 3]
        if max_length > 3:
            four_letter = line[i:i + 4]
        if max_length > 4:
            five_letter = line[i:i + 5]

        if three_letter in valid_numbers:
            number = valid_numbers[three_letter]
        if four_letter in valid_numbers:
            number = valid_numbers[four_letter]
        if five_letter in valid_numbers:
            number = valid_numbers[five_letter]
        if line[i].isnumeric():
            number = line[i]
        if left == '' and number != '':
            left = number
        elif number != '':
            right = number
    if right == '':
        return int(left + left)
    return int(left + right)

path = Path.cwd()/'Day1'/'d1p2testdata.txt'
with path.open() as test_data:
    total = 0
    for line in test_data:
        total += first_and_last_string(line)
assert total == 281

path = Path.cwd()/'Day1'/'d1p1data.txt'
with path.open() as test_data:
    total = 0
    for line in test_data:
        total += first_and_last_string(line)
print(total)