import sys
import math
import heapq

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

def get_area(i, j):
    if (heightmap[i][j] == 9):
        return 0
    heightmap[i][j] = 9
    return 1 + sum(get_area(di, dj) for di, dj in get_neighbors(i, j))

highest_areas = []

for i, row in enumerate(heightmap):
    for j, height in enumerate(row):
        if all(height < heightmap[di][dj] for di, dj in get_neighbors(i, j)):
            area = get_area(i, j)
            heapq.heappush(highest_areas, area)
        if (len(highest_areas) > 3):
            heapq.heappop(highest_areas)

print(math.prod(highest_areas))
