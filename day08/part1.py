import sys

file = open(f'{sys.path[0]}/input.txt', 'r')

total = 0

for line in file:
    data = line.split(' | ')
    for digit in data[1].split():
        digit_length = len(digit)
        if (digit_length in [2, 3, 4, 7]):
            total += 1

print(total)   
