import sys

def die():
    count = -1
    def roll():
        nonlocal count
        count = (count + 1) % 100
        return count + 1
    return roll

positions = [int(player.split()[-1]) - 1 for player in open(f'{sys.path[0]}/input.txt', 'r')]
scores = [0, 0]
roll = die()
turn = rolls = 0

while (max(scores) < 1000):
    total_steps = roll() + roll() + roll()

    positions[turn] = (positions[turn] + total_steps) % 10
    scores[turn] += positions[turn] + 1

    turn = (turn + 1) % 2
    rolls += 3

print(rolls * min(scores))
