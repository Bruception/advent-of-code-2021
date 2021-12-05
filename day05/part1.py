import sys
file = open(f'{sys.path[0]}/input.txt', 'r')

lines = []
max_x = 0
max_y = 0

for line in file:
    points = line.strip().split(' -> ')
    start_point = points[0].split(',')
    end_point = points[1].split(',')
    x1, y1 = int(start_point[0]), int(start_point[1])
    x2, y2 = int(end_point[0]), int(end_point[1])
    lines.append(((x1, y1), (x2, y2)))
    max_x = max(max_x, x1, x2)
    max_y = max(max_y, y1, y2)

grid = [[0 for j in range(max_x + 1)] for i in range(max_y + 1)]
intersection_points = 0

for line in lines:
    start, end = line
    x1, y1 = start
    x2, y2 = end
    if (x1 == x2):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            grid[y][x1] += 1
            intersection_points += 1 if grid[y][x1] == 2 else 0
    elif (y1 == y2):
        for x in range(min(x1, x2), max(x1, x2) + 1):
            grid[y1][x] += 1
            intersection_points += 1 if grid[y1][x] == 2 else 0

print(intersection_points)
