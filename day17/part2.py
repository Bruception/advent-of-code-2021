import sys
from re import findall

data = open(f'{sys.path[0]}/input.txt', 'r').read()
min_x, max_x, min_y, max_y = map(int, findall(r'-?\d+', data))

def simulate(vel_x, vel_y):
    x, y = 0, 0

    while (x <= max_x and y >= min_y):
        if (x >= min_x and y <= max_y):
            return True
        
        x += vel_x
        y += vel_y

        vel_x -= 1 if vel_x > 0 else 0
        vel_y -= 1

    return False

total = 0

for vel_x in range(1, max_x + 1):
    for vel_y in range(min_y, -min_y):
        did_hit = simulate(vel_x, vel_y)
        total += 1 if did_hit else 0

print(total)
