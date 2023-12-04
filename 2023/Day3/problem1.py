import re
from pathlib import Path

def is_part(line1, line2, line3):
    pass

path = Path.cwd()/'2023'/'Day3'/'d3p1testdata.txt'
with path.open() as test_data:
    for y, line in enumerate(test_data):
        line = line.strip()
        num_coords = []
        symbol_coords = []
        for x, char in enumerate(line):
            if char.isnumeric():
                