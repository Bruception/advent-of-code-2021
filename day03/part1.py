import sys
file = open(f'{sys.path[0]}/input.txt', 'r')

binary_strings = [line.strip() for line in file]
n = len(binary_strings)
one_counts = [0 for i in range(len(binary_strings[0]))]
for binary_string in binary_strings:
    for i, ch in enumerate(binary_string):
        one_counts[i] += 1 if ch == '1' else 0

gamma = []
epsilon = []
for i, freq in enumerate(one_counts):
    if (n - one_counts[i] > one_counts[i]):
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')

gamma = int(''.join(gamma), base=2)
epsilon = int(''.join(epsilon), base=2)

print(gamma * epsilon)