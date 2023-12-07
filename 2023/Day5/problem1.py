from pathlib import Path
import re

test_path = Path.cwd()/'2023'/'Day5'/'d5p1testdata.txt'
path = Path.cwd()/'2023'/'Day5'/'d5p1data.txt'

def get_seeds(first_line: str) -> list[int]:
    seeds = re.sub(r'(seeds: )', '', first_line.strip()).split(' ')
    return [int(seed) for seed in seeds]

def get_map_function(data):
    map_function = {}
    for line in data:
        line = line.strip()
        if line != '' and line[0].isalpha():
            map_name = line.split(' ')[0]
        if line != '' and line[0].isnumeric():
            line = line.split(' ')
            if map_name not in map_function.keys():
                map_function[map_name] = []
            map_function[map_name].append({
                'dest': int(line[0]),
                'src': int(line[1]),
                'range': int(line[2])
            })
    return map_function

def seed_transform(seed: list[int], transforms: list[dict]) -> int:
    for tf in transforms:
        src_range = range(tf['src'], tf['src'] + tf['range'] + 1)
        if seed in src_range:
            return (seed - tf['src']) + tf['dest']
    return seed
    
def lowest_location(path):
    with path.open() as data:
        seeds = get_seeds(data.readline())
        map_function = get_map_function(data)
    locations = []
    for seed in seeds:
        for transforms in map_function:
            seed = seed_transform(seed, map_function[transforms])
        locations.append(seed)

    return min(locations)
assert lowest_location(test_path) == 35
print(lowest_location(path))