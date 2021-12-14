import sys
from collections import Counter, defaultdict

polymer, _, *rules = open(f'{sys.path[0]}/input.txt', 'r').read().split('\n')
rules = dict(rule.split(' -> ') for rule in rules)

def get_bigrams(bigram_map, letter_frequencies):
    new_bigram_map = defaultdict(int)

    for bigram, frequency in bigram_map.items():
        middle = rules[bigram]
        new_bigram_map[bigram[0] + middle] += frequency
        new_bigram_map[middle + bigram[1]] += frequency
        letter_frequencies[middle] += frequency
    
    return new_bigram_map

bigram_map = Counter(a + b for a, b in zip(polymer, polymer[1:]))
letter_frequencies = Counter(polymer)

for i in range(40):
    bigram_map = get_bigrams(bigram_map, letter_frequencies)

frequency_values = letter_frequencies.values()

print(max(frequency_values) - min(frequency_values))
