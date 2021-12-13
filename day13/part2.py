import sys

file = open(f'{sys.path[0]}/input.txt', 'r')
all_lines = file.readlines()

def fold_along(axis, line_value):
    new_coordinates = set()

    for x, y in coordinates:
        if (axis == 'x' and x > line_value):
            x = 2 * line_value - x
        elif (axis == 'y' and y > line_value):
            y = 2 * line_value - y
        new_coordinates.add((x, y))

    return new_coordinates

coordinates = set([tuple(map(int, line.strip().split(','))) for line in all_lines if ',' in line])
flip_instructions = [line.strip().split()[2].split('=') for line in all_lines if 'fold' in line]

for axis, value in flip_instructions:
    coordinates = fold_along(axis, int(value))

def draw_coordinates():
    max_x = max(x for x, _ in coordinates) + 1
    max_y = max(y for _, y in coordinates) + 1

    grid = [[' '] * max_x for _ in range(max_y)]

    for x, y in coordinates:
        grid[y][x] = '#'
    
    print('\n', '\n'.join(''.join(row) for row in grid), sep='')

draw_coordinates()
