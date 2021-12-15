import sys
import heapq

grid = [list(map(int, row)) for row in open(f'{sys.path[0]}/input.txt', 'r').read().split('\n')]
rows, cols = len(grid), len(grid[0])

deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]

risk = {(i, j): sys.maxsize for i in range(rows) for j in range(cols)}
queue = [(0, (0, 0))]

while (queue):
    current_risk, position = heapq.heappop(queue)
    
    for di, dj in deltas:
        ni, nj = di + position[0], dj + position[1]
        neighbor_position = (ni, nj)
        if (neighbor_position in risk):
            new_risk = current_risk + grid[ni][nj]
            if (new_risk < risk[neighbor_position]):
                risk[neighbor_position] = new_risk
                heapq.heappush(queue, (new_risk, neighbor_position))

print(risk[(rows - 1, cols - 1)])
