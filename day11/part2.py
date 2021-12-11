import sys
from collections import deque

file = open(f'{sys.path[0]}/input.txt', 'r')
octopuses = [[int(ch) for ch in line.strip()] for line in file]
rows, cols = len(octopuses), len(octopuses[0])

neighbor_deltas = [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, 1), (1, -1), (-1, -1)]

def in_bounds(i, j):
    in_bounds_rows = i > -1 and i < rows
    in_bounds_cols = j > -1 and j < cols
    return in_bounds_rows and in_bounds_cols

def get_neighbors(i, j):
    return [(i + di, j + dj) for di, dj in neighbor_deltas if in_bounds(i + di, j + dj)]

def step():
    flashed = deque()
    flashes = 0

    for i in range(rows):
        for j in range(cols):
            octopuses[i][j] += 1
            if (octopuses[i][j] > 9):
                flashed.append((i, j))
                flashes += 1

    while (flashed):
        i, j = flashed.popleft()

        for ni, nj in get_neighbors(i, j):
            octopuses[ni][nj] += 1
            if (octopuses[ni][nj] == 10):
                flashed.append((ni, nj))
                flashes += 1

    return flashes == rows * cols

def cleanup():
    for i in range(rows):
        for j in range(cols):
            if (octopuses[i][j] > 9):
                octopuses[i][j] = 0

i = 0
did_flash = False

while (not did_flash):
    did_flash |= step()
    cleanup()
    i += 1

print(i)
