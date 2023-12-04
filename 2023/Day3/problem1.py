from pathlib import Path

def is_part(num_coord_tuple: tuple[tuple[int]], symbol_coords: set[tuple]) -> bool:
    test_coords = []
    for num_coord in num_coord_tuple:
        for x in range(num_coord[0] - 1, num_coord[0] + 2):
            for y in range(num_coord[1] - 1, num_coord[1] + 2):
                test_coords.append((x, y))
    test_coords = set(test_coords)

    for coord in test_coords:
        if coord in symbol_coords:
            return True
    return False

def get_parts_and_symbols(path):
    with path.open() as test_data:
        number_map = {}
        symbol_coords = set()
        for y, line in enumerate(test_data):
            line = line.strip()
            number_string = ''
            number_coords = []
            for x, char in enumerate(line):
                if char.isnumeric():
                    number_string += char
                    number_coords.append((x, y))
                if not char.isnumeric() and number_string != '':
                    number_map[tuple(number_coords)] = number_string
                    number_string = ''
                    number_coords = []
                if char != '.' and not char.isnumeric():
                    symbol_coords.add((x, y))
            if number_string != '':
                number_map[tuple(number_coords)] = number_string

    return number_map, symbol_coords
        
def sum_parts(number_map, symbol_coords):
    total = 0
    for potential_part_coord in number_map:
        if is_part(potential_part_coord, symbol_coords):
            total += int(number_map[potential_part_coord])

    return total


test_path = Path.cwd()/'Day3'/'d3p1testdata.txt'
test_number_map, test_symbol_coords = get_parts_and_symbols(test_path)
assert sum_parts(test_number_map, test_symbol_coords) == 4361

path = Path.cwd()/'Day3'/'d3p1data.txt'
number_map, symbol_coords = get_parts_and_symbols(path)
print(sum_parts(number_map, symbol_coords))
