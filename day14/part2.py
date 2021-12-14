import sys
from collections import Counter, defaultdict

file = open(f'{sys.path[0]}/input.txt', 'r')

polymer = file.readline().strip()
mappings = {pair: value for pair, value in [line.strip().split(' -> ') for line in file if '->' in line]}

def get_bigrams(bigram_map, letter_frequencies):
    new_bigram_map = defaultdict(int)

    for bigram, frequency in bigram_map.items():
        middle = mappings[bigram]
        new_bigram_map[bigram[0] + middle] += frequency
        new_bigram_map[middle + bigram[1]] += frequency
        letter_frequencies[middle] += frequency
    
    return new_bigram_map

bigram_map = Counter([str(polymer[i:i+2]) for i in range(len(polymer) - 1)])
letter_frequencies = Counter(polymer)

for i in range(40):
    bigram_map = get_bigrams(bigram_map, letter_frequencies)

frequency_values = letter_frequencies.values()

print(max(frequency_values) - min(frequency_values))
