import sys
from re import findall

data = open(f'{sys.path[0]}/input.txt', 'r').read()
min_x, max_x, min_y, max_y = map(int, findall(r'-?\d+', data))

def simulate(vel_x, vel_y):
    x, y, max_height = 0, 0, 0

    while (x <= max_x and y >= min_y):
        if (x >= min_x and y <= max_y):
            return max_height
        
        x += vel_x
        y += vel_y

        max_height = max(y, max_height)

        vel_x -= 1 if vel_x > 0 else 0
        vel_y -= 1

    return 0

global_max_height = 0

for vel_x in range(1, max_x + 1):
    for vel_y in range(min_y, -min_y):
        max_height = simulate(vel_x, vel_y)
        global_max_height = max(max_height, global_max_height)

print(global_max_height)
