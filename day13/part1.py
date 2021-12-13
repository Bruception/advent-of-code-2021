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

for axis, value in flip_instructions[:1]:
    coordinates = fold_along(axis, int(value))

print(len(coordinates))
