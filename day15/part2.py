import sys
import heapq

grid = [list(map(int, row)) for row in open(f'{sys.path[0]}/input.txt', 'r').read().split('\n')]
rows, cols, extension = len(grid), len(grid[0]), 5
extended_rows, extended_cols = rows * extension, cols * extension

def get_risk(i, j):
    risk = ((i // rows) + (j // cols) + grid[i % rows][j % cols]) % 9
    return 9 if risk == 0 else risk

deltas = [(-1, 0), (0, -1), (1, 0), (0, 1)]

risk = {(i, j): sys.maxsize for i in range(extended_rows) for j in range(extended_cols)}
queue = [(0, (0, 0))]

while (queue):
    current_risk, position = heapq.heappop(queue)

    for di, dj in deltas:
        neighbor_position = (di + position[0], dj + position[1])
        if (neighbor_position in risk):
            new_risk = current_risk + get_risk(*neighbor_position)
            if (new_risk < risk[neighbor_position]):
                risk[neighbor_position] = new_risk
                heapq.heappush(queue, (new_risk, neighbor_position))

print(risk[(extended_rows - 1, extended_cols - 1)])
