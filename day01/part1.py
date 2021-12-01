import sys

file = open(f'{sys.path[0]}/input.txt', 'r')
numbers = [int(line) for line in file]
print(sum(1 if (numbers[i] > numbers[i - 1]) else 0 for i in range(1, len(numbers))))
