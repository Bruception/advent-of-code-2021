import sys
from collections import deque

file = open(f'{sys.path[0]}/input.txt', 'r')

possibilities = {
    2: [1],
    3: [7],
    4: [4],
    5: [2, 3, 5],
    6: [0, 6, 9],
    7: [8]
}

contains = {
    0: [1, 7],
    1: [],
    2: [],
    3: [1, 7],
    4: [1],
    5: [],
    6: [5],
    7: [1],
    8: [0, 1, 2, 3, 4, 5, 6, 7, 9],
    9: [1, 3, 4, 5, 7],
}

def decode(signal_patterns, digits):
    signal_patterns = [''.join(sorted(pattern)) for pattern in signal_patterns]
    digits = [''.join(sorted(digit)) for digit in digits]

    table = {}
    solved = deque()
    for pattern in signal_patterns:
        picked = possibilities[len(pattern)]
        table[pattern] = set(picked)
        if (len(picked) == 1):
            solved.append((set(pattern), picked[0]))

    while (solved):
        pattern, current_number = solved.popleft()
        for unknown_pattern, choices in table.items():
            if (len(choices) == 1):
                continue
            
            to_remove = []

            unknown_pattern_set = set(unknown_pattern)

            for choice in choices:
                within = current_number in contains[choice]
                contained_in_pattern = pattern.issubset(unknown_pattern_set)
                if ((not within and contained_in_pattern) or (within and not contained_in_pattern)):
                    to_remove.append(choice)
            
            choices.difference_update(to_remove)
            
            if (len(choices) == 1):
                solved.append((unknown_pattern_set, list(choices)[0]))

    nines_pattern = set([k for k, v in table.items() if 9 in v][0])
    for pattern, choices in table.items():
        if (len(choices) == 2):
            choices.discard(2 if set(pattern).issubset(nines_pattern) else 5)

    mapping = {key: value.pop() for key, value in table.items()}
    return int(''.join([str(mapping[digit]) for digit in digits]))

total = 0

for line in file:
    data = line.strip().split(' | ')
    signal_patterns = data[0].split()
    digits = data[1].split()
    total += decode(signal_patterns, digits)

print(total)
