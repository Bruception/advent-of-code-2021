import sys
from collections import defaultdict

file = open(f'{sys.path[0]}/input.txt', 'r')

adj_list = defaultdict(list)
small_caves = set()

for line in file:
    edge = line.strip().split('-')
    a, b = edge[0], edge[1]
    adj_list[a].append(b)
    adj_list[b].append(a)

    if (a.lower() == a):
        small_caves.add(a)
    if (b.lower() == b):
        small_caves.add(b)

def find_paths(current, visited):
    if (current in visited):
        return 0

    if (current == 'end'):
        return 1
    
    if (current in small_caves):
        visited.add(current)

    total_paths = 0

    for neighbor in adj_list[current]:
        total_paths += find_paths(neighbor, visited)
    
    visited.discard(current)
    
    return total_paths

num_paths = find_paths('start', set())
print(num_paths)
