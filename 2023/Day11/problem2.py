from pathlib import Path

test_path = Path.cwd()/'Day9'/'d9p1testdata.txt'
path = Path.cwd()/'Day9'/'d9p1data.txt'

def get_sequence(seq):
    new_seq = []
    for i in range(len(seq) - 1):
        new_seq.append(seq[i + 1] - seq[i])
    return new_seq

def next_val_total(path):
    total = 0
    with path.open() as data:
        for line in data:
            seqs = [[int(num) for num in line.strip().split(' ')]]
            while seqs[-1] != [0]*len(seqs[-1]):
                seqs.append(get_sequence(seqs[-1]))
            seqs[-1].append(0)
            for i in range(len(seqs) - 2, -1, -1):
                seqs[i].append(seqs[i+1][-1] + seqs[i][-1])
            total += seqs[0][-1]

    return total

def prev_value_total(path):
    total = 0
    with path.open() as data:
        for line in data:
            seqs = [[int(num) for num in line.strip().split(' ')]]
            while seqs[-1] != [0]*len(seqs[-1]):
                seqs.append(get_sequence(seqs[-1]))
            seqs[-1].append(0)
            for i in range(len(seqs) - 2, -1, -1):
                a = seqs[i]
                b = seqs[i+1]
                seqs[i].append(seqs[i][0] - seqs[i+1][-1])
            total += seqs[0][-1]

    return total

assert next_val_total(test_path) == 114
assert prev_value_total(test_path) == 2
print(prev_value_total(path))