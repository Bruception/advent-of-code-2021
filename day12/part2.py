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

def find_paths(current, visited, visited_small_twice):
    if (current == 'end'):
        return 1
    
    if (visited[current] > 0 and visited_small_twice):
        return 0
    
    if (current in small_caves):
        visited[current] += 1
        visited_small_twice |= visited[current] == 2

    total_paths = 0

    for neighbor in adj_list[current]:
        if (neighbor != 'start'):
            total_paths += find_paths(neighbor, visited, visited_small_twice)
            
    visited[current] -= 1
    
    return total_paths

num_paths = find_paths('start', defaultdict(int), False)
print(num_paths)
