from pathlib import Path

def get_adj_stars(num_coord_tuple: tuple[tuple[int]], star_coords: set[tuple]) -> bool:
    test_coords = []
    for num_coord in num_coord_tuple:
        for x in range(num_coord[0] - 1, num_coord[0] + 2):
            for y in range(num_coord[1] - 1, num_coord[1] + 2):
                test_coords.append((x, y))
    test_coords = set(test_coords)

    adj_stars = []
    for coord in test_coords:
        if coord in star_coords:
            adj_stars.append(coord)
    return adj_stars

def get_parts_and_stars(path):
    with path.open() as test_data:
        number_map = {}
        star_coords = set()
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
                if char == '*':
                    star_coords.add((x, y))
            if number_string != '':
                number_map[tuple(number_coords)] = number_string

    return number_map, star_coords
        
def get_gear_dict(number_map, star_coords):
    gear_dict = {}
    for part in number_map:
        gear_dict[part] = get_adj_stars(part, star_coords)
    return gear_dict

def find_gears(gear_dict, number_map):
    total = 0
    tested_gears = []
    for gear1 in gear_dict:
        test_gear = number_map[gear1]
        stars = gear_dict[gear1]
        tested_gears.append(gear1)
        for star in stars:
            for gear2 in gear_dict:
                test_gear2 = number_map[gear2]
                if star in gear_dict[gear2] and gear2 not in tested_gears:
                    total += int(test_gear) * int(number_map[gear2])        
                    tested_gears.append(gear2) 
    return total
# def sum_gears(number_map, star_coords):
#     total = 0
#     gear_dict = get_gear_dict(number_map, star_coords)
#     for potential_part_coord in number_map:
        
#         if is_part(potential_part_coord, star_coords):
#             total += int(number_map[potential_part_coord])

#     return total


test_path = Path.cwd()/'Day3'/'d3p1testdata.txt'
test_number_map, test_star_coords = get_parts_and_stars(test_path)
test_gear_dict = get_gear_dict(test_number_map, test_star_coords)
assert find_gears(test_gear_dict, test_number_map) == 467835

path = Path.cwd()/'Day3'/'d3p1data.txt'
number_map, star_coords = get_parts_and_stars(path)
gear_dict = get_gear_dict(number_map, star_coords)
print(find_gears(gear_dict, number_map))