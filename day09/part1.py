import sys

file = open(f'{sys.path[0]}/input.txt', 'r')

heightmap = [[int(height) for height in line.strip()] for line in file]
rows, cols = len(heightmap), len(heightmap[0])

def get_neighbors(i, j):
    neighbors = []
    
    if (i > 0):
        neighbors.append(heightmap[i - 1][j])
    if (j > 0):
        neighbors.append(heightmap[i][j - 1])
    if (i + 1 < rows):
        neighbors.append(heightmap[i + 1][j])
    if (j + 1 < cols):
        neighbors.append(heightmap[i][j + 1])

    return neighbors

risk_level = sum(
    height + 1
    for i, row in enumerate(heightmap)
    for j, height in enumerate(row)
    if all(height < neighbor_height for neighbor_height in get_neighbors(i, j))
)

print(risk_level)
