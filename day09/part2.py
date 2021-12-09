import sys
import math
import heapq
from collections import deque

file = open(f'{sys.path[0]}/input.txt', 'r')

heightmap = [[int(height) for height in line.strip()] for line in file]
rows, cols = len(heightmap), len(heightmap[0])

def get_neighbors(i, j):
    neighbors = []
    
    if (i > 0):
        neighbors.append((i - 1, j))
    if (j > 0):
        neighbors.append((i, j - 1))
    if (i + 1 < rows):
        neighbors.append((i + 1, j))
    if (j + 1 < cols):
        neighbors.append((i, j + 1))

    return neighbors

low_points = deque([
    (i, j)
    for i, row in enumerate(heightmap)
    for j, height in enumerate(row)
    if all(height < heightmap[di][dj] for di, dj in get_neighbors(i, j))
])

def get_area(i, j, visited):
    key = (i, j)
    if (key in visited):
        return 0
    visited.add(key)

    total_area = 1

    for di, dj in get_neighbors(i, j):
        if (heightmap[di][dj] != 9):
            total_area += get_area(di, dj, visited)

    return total_area

highest_areas = []

for i, j in low_points:
    area = get_area(i, j, set())
    heapq.heappush(highest_areas, area)
    if (len(highest_areas) > 3):
        heapq.heappop(highest_areas)

print(math.prod(highest_areas))
