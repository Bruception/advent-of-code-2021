import sys
from math import ceil
from functools import reduce

def split(num, split_index):
    new_num = num[:split_index]

    token = num[split_index]
    a = token >> 1
    b = ceil(token / 2)

    new_num.extend(['[', a, b, ']'])    
    new_num.extend(num[split_index+1:])

    return new_num

def explode(num, explode_index):
    new_num = num[:explode_index]

    right, left, _ = [new_num.pop() for _ in range(3)]

    for j in range(len(new_num) - 1, -1, -1):
        if (isinstance(new_num[j], int)):
            new_num[j] += left
            break

    for j in range(explode_index + 1, len(num)):
        if (isinstance(num[j], int)):
            num[j] += right
            break

    new_num.append(0)
    new_num.extend(num[explode_index+1:])

    return new_num

def can_explode(num):
    depth = 0
    for i, token in enumerate(num):
        if (token == '['):
            depth += 1
        elif (token == ']'):
            depth -= 1
            if (depth >= 4):
                return i
    return -1

def can_split(num):
    for i, token in enumerate(num):
        if (isinstance(token, int) and token >= 10):
            return i
    return -1

def simplify(num):
    explode_index, split_index = 0, 0
    while (explode_index != -1 or split_index != -1):
        explode_index, split_index = can_explode(num), can_split(num)

        if (explode_index != -1):
            num = explode(num, explode_index)
        elif (split_index != -1):
            num = split(num, split_index)

    return ''.join(str(token) for token in num)

def normalize(num):
    return [int(token) if token.isdigit() else token for token in num if token != ',']

def add(a, b):
    return simplify(normalize(f'[{a}{b}]'))

def magnitude(num):
    num = normalize(num)

    stack = []

    for token in num:
        stack.append(token)
        if (token == ']'):
            _, right, left, _ = [stack.pop() for _ in range(4)]
            stack.append((3 * left) + (2 * right))

    return stack.pop()

snail_numbers = open(f'{sys.path[0]}/input.txt', 'r').read().split('\n')
total = reduce(add, snail_numbers)

print(magnitude(total))
