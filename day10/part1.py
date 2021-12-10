import sys

file = open(f'{sys.path[0]}/input.txt', 'r')

score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}
pairing = {')': '(', ']': '[', '}': '{', '>': '<'}

def get_score(line):
    stack = []
    for ch in line:
        if (ch in '([{<'):
            stack.append(ch)
        else:
            top = stack.pop() if stack else None
            if (top != pairing[ch]):
                return score_map[ch]
    return 0

print(sum(get_score(line.strip()) for line in file))
