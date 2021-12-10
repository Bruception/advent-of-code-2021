import sys

file = open(f'{sys.path[0]}/input.txt', 'r')

pairing = {')': '(', ']': '[', '}': '{', '>': '<'}
score_map = {'(': 1, '[': 2, '{': 3, '<': 4}

def get_completion_score(line):
    stack = []
    for ch in line:
        if (ch in score_map):
            stack.append(ch)
        else:
            top = stack.pop() if stack else None
            if (top != pairing[ch]):
                return 0
    
    score = 0
    for ch in reversed(stack):
        score *= 5
        score += score_map[ch]

    return score

lines = [line.strip() for line in file]
line_scores = [get_completion_score(line) for line in lines]
incomplete_scores = sorted([score for score in line_scores if score != 0])

print(incomplete_scores[len(incomplete_scores) >> 1])
