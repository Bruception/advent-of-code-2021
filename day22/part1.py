import re
import sys

steps = [
    (line.split(' ')[0], tuple(map(int, re.findall(r'-?\d+', line))))
    for line in open(f'{sys.path[0]}/input.txt', 'r')
]

cubes = set()

for step_type, area in steps:
    for x in range(max(area[0], -50), min(area[1], 50) + 1):
        for y in range(max(area[2], -50), min(area[3], 50) + 1):
            for z in range(max(area[4], -50), min(area[5], 50) + 1):
                (cubes.add if step_type == 'on' else cubes.discard)((x, y, z))

print(len(cubes))
