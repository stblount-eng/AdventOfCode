from pathlib import Path
from collections import Counter
import re
from math import gcd

test_path = Path.cwd()/'2023'/'Day8'/'d8p2testdata.txt'
path = Path.cwd()/'2023'/'Day8'/'d8p1data.txt'

def number_of_steps_single(name, nodes, instructions):
    steps = 1
    i = 0
    while True:
        name = nodes[name][instructions[i]]
        if name[2] == 'Z':
            return steps
        i += 1
        steps += 1
        if i == len(instructions):
            i = 0

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
    names = [node for node in nodes.keys() if node[2]=='A']
    min_steps = []
    for name in names:
        min_steps.append(number_of_steps_single(name, nodes, instructions))
    lcm = 1
    for step in min_steps:
        lcm = lcm*step//gcd(lcm, step)
    return lcm

assert number_of_steps(test_path) == 6
print(number_of_steps(path))