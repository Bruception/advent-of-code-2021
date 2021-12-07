import sys
import math

file = open(f'{sys.path[0]}/input.txt', 'r')
crab_positions = [int(position) for position in file.readline().strip().split(',')]

def get_fuel_cost(position, i):
    distance = abs(position - i)
    return distance * ((distance + 1) / 2)

def total_cost_here(i):
    return sum(get_fuel_cost(position, i) for position in crab_positions)

l = min(crab_positions)
r = max(crab_positions)
best_cost_so_far = math.inf

while (l < r):
    mid = ((r - l) >> 1) + l
    cost_here = total_cost_here(mid)
    right_cost = total_cost_here(mid + 1)

    best_cost_so_far = min(cost_here, best_cost_so_far)

    if (right_cost >= cost_here):
        r = mid - 1
    else:
        l = mid + 1

print(int(best_cost_so_far))
