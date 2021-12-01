import sys

file = open(f'{sys.path[0]}/input.txt', 'r')
numbers = [int(line) for line in file]
windows = [numbers[i] + numbers[i + 1] + numbers[i + 2] for i in range(0, len(numbers) - 2)]
print(sum(1 if (windows[i] > windows[i - 1]) else 0 for i in range(1, len(windows))))
