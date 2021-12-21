import sys
from functools import cache
from itertools import product

possible_rolls = list(product([1, 2, 3], repeat=3))

@cache
def dirac_dice(p1, p2, s1, s2):
    if (s2 >= 21):
        return (0, 1)

    total_p1_wins = total_p2_wins = 0
    
    for r1, r2, r3 in possible_rolls:
        new_position = (p1 + r1 + r2 + r3) % 10
        new_score = s1 + new_position + 1

        p2_wins, p1_wins = dirac_dice(p2, new_position, s2, new_score)

        total_p1_wins += p1_wins
        total_p2_wins += p2_wins
    
    return (total_p1_wins, total_p2_wins)
        
p1, p2 = (int(player.split()[-1]) - 1 for player in open(f'{sys.path[0]}/input.txt', 'r'))

print(max(dirac_dice(p1, p2, 0, 0)))
