from pathlib import Path
from collections import Counter
import re

test_path1 = Path.cwd()/'2023'/'Day8'/'d8p1testdata1.txt'
test_path2 = Path.cwd()/'2023'/'Day8'/'d8p1testdata2.txt'
path = Path.cwd()/'2023'/'Day8'/'d8p1data.txt'

def number_of_steps(path):
    with path.open() as data:
        instructions = data.read().split('\n\n')
    nodes_pre = instructions.pop().split('\n')
    instructions = instructions[0]
    nodes = {}
    for node in nodes_pre:
        vals = re.findall(r'([A-Z]{3})', node)
        nodes[vals[0]] = {
            'L': vals[1],
            'R': vals[2]
        }
    i = 0
    start_names = re.findall(r'([A-Z]{2})A', nodes.keys())
    steps = 1
    while True:
        name = nodes[name][instructions[i]]
        if name == 'ZZZ':
            return steps
        i += 1
        steps += 1
        if i == len(instructions):
            i = 0

assert number_of_steps(test_path1) == 2
assert number_of_steps(test_path2) == 6
print(number_of_steps(path))