import sys
file = open(f'{sys.path[0]}/input.txt', 'r')

depth = 0
horizontal = 0
aim = 0

for instruction in file:
    data = instruction.split(' ')
    direction = data[0]
    amount = int(data[1])

    if (direction == 'forward'):
        horizontal += amount
        depth += aim * amount
    elif (direction == 'down'):
        aim += amount
    elif(direction == 'up'):
        aim -= amount

print(depth * horizontal)

