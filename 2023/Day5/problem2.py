from pathlib import Path
import re
import cProfile

test_path = Path.cwd()/'2023'/'Day5'/'d5p1testdata.txt'
path = Path.cwd()/'2023'/'Day5'/'d5p1data.txt'

def get_seed_generator(seed_start, seed_end):
    seed = seed_start
    while seed <= seed_end:
        yield seed
        seed += 1

def get_seeds(first_line: str) -> list[tuple]:
    line = re.sub(r'(seeds: )', '', first_line.strip()).split(' ')
    line = [int(val) for val in line]
    seeds = []
    for i, val in enumerate(line):
        if i%2 == 0:
            seed_start = val
        else:
            seeds.append((seed_start, seed_start + val))
    return seeds

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
        src = tf['src']
        dest = tf['dest']
        rng = tf['range']
        if seed <= src + rng and seed >= src:
            return (seed - tf['src']) + tf['dest']
    return seed
    
def lowest_location(path):
    with path.open() as data:
        seed_ranges = get_seeds(data.readline())
        map_function = get_map_function(data)
    min_location = float('inf')
    for seed_range in seed_ranges:
        seed_gen = get_seed_generator(seed_range[0], seed_range[1])
        for seed in seed_gen:
            for transforms in map_function:
                seed = seed_transform(seed, map_function[transforms])
            if seed < min_location:
                min_location = seed

    return min_location
# assert lowest_location(test_path) == 46
# print(lowest_location(path))
cProfile.run('lowest_location(path)')