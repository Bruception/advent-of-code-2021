import sys
from collections import Counter

file = open(f'{sys.path[0]}/input.txt', 'r')

polymer = file.readline().strip()
mappings = {pair: value for pair, value in [line.strip().split(' -> ') for line in file if '->' in line]}

def step(polymer):
    new_polymer = []

    for i in range(len(polymer) - 1):
        key = str(polymer[i:i+2])
        new_polymer.append(polymer[i])
        if (key in mappings):
            new_polymer.append(mappings[key])
    
    new_polymer.append(polymer[-1])

    return ''.join(new_polymer)

for i in range(10):
    polymer = step(polymer)

counter = Counter(polymer).values()

print(max(counter) - min(counter))
